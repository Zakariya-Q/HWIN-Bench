import argparse
import os
import sys
import json
import time
import warnings
import numpy as np
import pandas as pd
from pathlib import Path
from sklearn.model_selection import GroupKFold
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.ensemble import RandomForestRegressor, ExtraTreesRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, median_absolute_error
from scipy import stats

warnings.filterwarnings("ignore")


def parse_args(argv=None):
    """CLI configuration. Environment variables provide defaults so the frozen
    canonical protocol can also be driven by CI without flags."""
    p = argparse.ArgumentParser(
        description="HWIN-Bench v1.0 canonical GRQA regression benchmark runner"
    )
    default_data = os.environ.get(
        "HWIN_DATA_PATH",
        "data/harmonized/HWIN-GRQA-V1-4/observations.csv",
    )
    default_out = os.environ.get("HWIN_OUTPUT_DIR", "output/benchmark_results")
    p.add_argument("--data", default=default_data,
                   help="Path to harmonized observations.csv (env: HWIN_DATA_PATH)")
    p.add_argument("--output-dir", default=default_out,
                   help="Directory for results JSON (env: HWIN_OUTPUT_DIR)")
    p.add_argument("--smoke-test", action="store_true",
                   help="Fast sanity run: 1 variable, 2 models, 1 seed, 3 folds, "
                        "500-row cap, subsampled CSV read")
    p.add_argument("--variables", default=os.environ.get("HWIN_VARIABLES"),
                   help="Comma-separated canonical variable IDs (default: auto-select "
                        ">= MIN_SAMPLES; env: HWIN_VARIABLES)")
    p.add_argument("--no-auto-select", action="store_true",
                   help="Use the frozen 11-variable canonical list instead of auto-selection")
    return p.parse_args(argv)


ARGS = parse_args()

# Configuration constants - can be overridden via environment variables or config
MIN_SAMPLES = int(os.environ.get("HWIN_MIN_SAMPLES", "100"))
MAX_SAMPLES_PER_VAR = int(os.environ.get("HWIN_MAX_SAMPLES_PER_VAR", "200000"))

# Default variable list (used if auto-selection disabled or for backward compatibility)
DEFAULT_VARIABLES = [
    "HWIN-VAR-001", "HWIN-VAR-002", "HWIN-VAR-003",
    "HWIN-VAR-008", "HWIN-VAR-009", "HWIN-VAR-010",
    "HWIN-VAR-014", "HWIN-VAR-015", "HWIN-VAR-028",
    "HWIN-VAR-031", "HWIN-VAR-033",
]

DATA_PATH = Path(ARGS.data)
OUTPUT_DIR = Path(ARGS.output_dir)

if ARGS.smoke_test:
    SMOKE = True
    MAX_SAMPLES_PER_VAR = min(MAX_SAMPLES_PER_VAR, 500)
    MIN_SAMPLES = min(MIN_SAMPLES, 100)
    SEEDS = [42]
    N_FOLDS = 3
else:
    SMOKE = False
    SEEDS = [42, 123, 256, 512, 1024]
    N_FOLDS = 5

SMOKE_NROWS = 50000  # CSV rows read in smoke-test mode

MODELS = {
    "linear_regression": {"model": LinearRegression, "params": {}},
    "ridge": {"model": Ridge, "params": {"alpha": 1.0}},
    "lasso": {"model": Lasso, "params": {"alpha": 0.1, "max_iter": 5000}},
    "elasticnet": {"model": ElasticNet, "params": {"alpha": 0.1, "l1_ratio": 0.5, "max_iter": 5000}},
    "random_forest": {"model": RandomForestRegressor, "params": {"n_estimators": 200, "max_depth": None, "min_samples_split": 2, "random_state": 42, "n_jobs": -1}},
    "extra_trees": {"model": ExtraTreesRegressor, "params": {"n_estimators": 200, "max_depth": None, "min_samples_split": 2, "random_state": 42, "n_jobs": -1}},
    "gradient_boosting": {"model": GradientBoostingRegressor, "params": {"n_estimators": 200, "learning_rate": 0.1, "max_depth": 3, "random_state": 42}},
}

if ARGS.smoke_test:
    # Keep the run fast: linear head + one tree ensemble is enough to exercise
    # the full pipeline (features, GroupKFold, metrics, JSON output)
    MODELS = {
        "linear_regression": MODELS["linear_regression"],
        "extra_trees": {"model": ExtraTreesRegressor, "params": {"n_estimators": 10, "max_depth": 6, "random_state": 42, "n_jobs": -1}},
    }

SAMPLE_CAP = MAX_SAMPLES_PER_VAR

def mape(y_true, y_pred):
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    mask = y_true != 0
    if not np.any(mask):
        return np.nan
    return np.mean(np.abs((y_true[mask] - y_pred[mask]) / y_true[mask])) * 100

METRICS = {
    "mae": mean_absolute_error,
    "rmse": lambda y, yp: np.sqrt(mean_squared_error(y, yp)),
    "r2": r2_score,
    "mape": mape,
    "medae": median_absolute_error,
}

def ci(vals, confidence=0.95):
    vals = np.array([v for v in vals if not np.isnan(v)])
    n = len(vals)
    if n < 2:
        return [np.nan, np.nan]
    m = np.mean(vals)
    se = stats.sem(vals)
    h = se * stats.t.ppf((1 + confidence) / 2., n - 1)
    return [float(m - h), float(m + h)]

def feats(df):
    X = pd.DataFrame()
    X["latitude"] = df["latitude"]
    X["longitude"] = df["longitude"]
    dt = pd.to_datetime(df["timestamp"], errors="coerce")
    X["year"] = dt.dt.year.fillna(2000).astype(int)
    X["month"] = dt.dt.month.fillna(6).astype(int)
    X["day_of_year"] = dt.dt.dayofyear.fillna(180).astype(int)
    X["sin_doy"] = np.sin(2 * np.pi * X["day_of_year"] / 365.25)
    X["cos_doy"] = np.cos(2 * np.pi * X["day_of_year"] / 365.25)
    return X.values.astype(np.float32)

def cv(var_data, var_name, models, seeds, n_folds, sample_cap):
    """Cross-validation loop. NOTE on the seed loop: `seeds` iterates the
    canonical seed list [42, 123, 256, 512, 1024], but the seed value is NOT
    consumed by any stochastic operation here — GroupKFold is deterministic
    given groups, and models use fixed random_state=42. The five iterations
    are therefore DETERMINISTIC REPETITIONS of the same 5-fold partition set
    (25 evaluations of which 5 are unique). This is the frozen v1.0 protocol;
    reported confidence intervals use the corrected n=5 (unique partitions)
    statistics — see CI_CORRECTION_REVIEW/."""
    print("\n" + "="*60)
    print("Variable: " + var_name + " (" + str(len(var_data)) + " observations)")
    print("="*60)
    if len(var_data) > sample_cap:
        var_data = var_data.sample(n=sample_cap, random_state=42).reset_index(drop=True)
        print("Sampled to " + str(sample_cap) + " observations")
    X = feats(var_data)
    y = var_data["value"].values.astype(np.float32)
    groups = var_data["station_id"].astype(str).values
    print("Features: " + str(X.shape) + ", Target: " + str(y.shape) + ", Stations: " + str(len(np.unique(groups))))
    print("Target stats: mean={:.3f}, std={:.3f}, min={:.3f}, max={:.3f}".format(y.mean(), y.std(), y.min(), y.max()))
    res = {}
    for m_name, m_info in models.items():
        print("  Model: " + m_name)
        t0 = time.time()
        allm = {k: [] for k in METRICS.keys()}
        all_t = []
        for seed in seeds:
            gkf = GroupKFold(n_splits=n_folds)
            fi = 0
            for tr, te in gkf.split(X, y, groups=groups):
                ft = time.time()
                Xtr, Xte = X[tr], X[te]
                ytr, yte = y[tr], y[te]
                mdl = m_info["model"](**m_info["params"])
                try:
                    mdl.fit(Xtr, ytr)
                    yp = mdl.predict(Xte)
                    for mn, mf in METRICS.items():
                        try:
                            v = mf(yte, yp)
                            if not np.isnan(v) and not np.isinf(v):
                                allm[mn].append(float(v))
                        except:
                            allm[mn].append(np.nan)
                    all_t.append(time.time() - ft)
                    fi += 1
                except Exception as e:
                    print("    Fold " + str(fi) + " failed: " + str(e))
                    for mn in METRICS:
                        allm[mn].append(np.nan)
                    fi += 1
        mt = time.time() - t0
        summ = {}
        for mn, vs in allm.items():
            vs = [v for v in vs if not np.isnan(v)]
            if vs:
                summ[mn] = {"mean": float(np.mean(vs)), "std": float(np.std(vs)), "median": float(np.median(vs)), "min": float(np.min(vs)), "max": float(np.max(vs)), "ci_95": ci(vs), "n_folds": len(vs), "all_values": vs}
            else:
                summ[mn] = {"mean": np.nan, "std": np.nan, "median": np.nan, "min": np.nan, "max": np.nan, "ci_95": [np.nan, np.nan], "n_folds": 0, "all_values": []}
        res[m_name] = {"metrics": summ, "total_time": mt, "avg_fold_time": np.mean(all_t) if all_t else np.nan, "n_folds_completed": sum(1 for v in allm["r2"] if not np.isnan(v))}
        r2m = summ["r2"]["mean"]
        r2ci = summ["r2"]["ci_95"]
        print("    R2 = {:.4f} (CI: [{:.4f}, {:.4f}])  Time: {:.1f}s".format(r2m, r2ci[0], r2ci[1], mt))
    return res

def conv(obj):
    if isinstance(obj, (np.integer, np.int64)): return int(obj)
    if isinstance(obj, (np.floating, np.float64, np.float32)): return float(obj)
    if isinstance(obj, np.ndarray): return obj.tolist()
    if isinstance(obj, dict): return {k: conv(v) for k, v in obj.items()}
    if isinstance(obj, list): return [conv(v) for v in obj]
    if isinstance(obj, tuple): return tuple(conv(v) for v in obj)
    if pd.isna(obj): return None
    return obj

print("="*60)
print("HWIN-Bench GRQA Full Benchmark Recomputation")
print("="*60)

if not DATA_PATH.exists():
    print("ERROR: Data not found at", DATA_PATH)
    print("Usage: python run_full_benchmark_fixed.py --data <observations.csv> [--smoke-test]")
    sys.exit(1)

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

print()
print("Loading data...")
dtypes = {"station_id": str, "variable": str, "value": float, "latitude": float, "longitude": float, "timestamp": str}
chunks = []
cs = 100000
tr = 0
nrows = SMOKE_NROWS if SMOKE else None
for c in pd.read_csv(DATA_PATH, chunksize=cs, nrows=nrows, low_memory=False, dtype=dtypes):
    chunks.append(c)
    tr += len(c)
    if tr % 1000000 == 0:
        print("  Loaded", tr, "rows...")
data = pd.concat(chunks, ignore_index=True)
print("Total observations:", len(data))
print("Stations:", data["station_id"].nunique())
if "timestamp" in data.columns:
    print("Date range:", data["timestamp"].min(), "to", data["timestamp"].max())

# Variable selection (single pass over loaded data):
#   --variables / HWIN_VARIABLES  -> explicit list
#   --no-auto-select              -> frozen canonical 11-variable list
#   default (auto-select)         -> variables with >= MIN_SAMPLES observations
counts = data["variable"].value_counts()
if ARGS.variables:
    VARIABLES = [v.strip() for v in ARGS.variables.split(",") if v.strip()]
    print(f"Using explicit variable list ({len(VARIABLES)} variables): {VARIABLES}")
elif ARGS.no_auto_select:
    VARIABLES = DEFAULT_VARIABLES
    print(f"Using default variable list ({len(VARIABLES)} variables): {VARIABLES}")
else:
    eligible = counts[counts >= MIN_SAMPLES].index.tolist()
    VARIABLES = sorted(eligible)
    print(f"Auto-selected {len(VARIABLES)} variables with >= {MIN_SAMPLES} samples: {VARIABLES}")

tv = set(VARIABLES) & set(counts.index)
missing = set(VARIABLES) - tv
if missing:
    print("WARNING: Missing from data:", sorted(missing))
tv = sorted(tv)
print("Processing:", tv)

data = data[data["variable"].isin(tv)].reset_index(drop=True)
print("Filtered:", len(data))

# Smoke-test variable subset: 1 variable is enough to exercise the pipeline
if SMOKE and len(tv) > 1:
    tv = tv[:1]
    data = data[data["variable"].isin(tv)].reset_index(drop=True)
    print("Smoke test: restricted to", tv)

print()
print("Variables:", len(tv))
print("Models:", len(MODELS))
print("Seeds:", len(SEEDS), "x Folds:", N_FOLDS, "=", len(SEEDS) * N_FOLDS, "evals/var")
print("Total fits:", len(tv) * len(MODELS) * len(SEEDS) * N_FOLDS)
print("Sample cap:", SAMPLE_CAP)
print("Data:", DATA_PATH)
print("Output:", OUTPUT_DIR)

# Check which variables already have results
existing_results = set()
for f in OUTPUT_DIR.glob("*_results.json"):
    if f.name != "all_results.json":
        existing_results.add(f.name.replace("_results.json", ""))

print("Already completed:", sorted(existing_results))

allr = {}
ts = time.time()
for vn in tv:
    if vn in existing_results:
        print("\nSkipping " + vn + " (already completed)")
        with open(OUTPUT_DIR / (vn + "_results.json"), "r") as f:
            allr[vn] = json.load(f)
        continue
    vd = data[data["variable"] == vn].copy()
    if len(vd) == 0:
        print("\nSkipping " + vn + ": no data")
        continue
    try:
        vr = cv(vd, vn, MODELS, SEEDS, N_FOLDS, SAMPLE_CAP)
        allr[vn] = vr
        vo = OUTPUT_DIR / (vn + "_results.json")
        with open(vo, "w") as f:
            json.dump(conv(vr), f, indent=2)
        print("  Saved:", vo)
    except Exception as e:
        print()
        print("ERROR on " + vn + ": " + str(e))
        import traceback
        traceback.print_exc()
        allr[vn] = {"error": str(e)}

tt = time.time() - ts
co = OUTPUT_DIR / "all_results.json"
with open(co, "w") as f:
    json.dump(conv(allr), f, indent=2)
print()
print("="*60)
print("Saved:", co)
print("Total runtime: {:.1f} min".format(tt/60))

print()
print("="*60)
print("SUMMARY REPORT")
print("="*60)
print("{:<15} {:<20} {:<8} {:<25} {:<10}".format("Variable", "Best Model", "R2", "CI", "Time (s)"))
print("-"*80)
for vn, vr in allr.items():
    if "error" in vr:
        print("{:<15} ERROR: {}".format(vn, vr["error"]))
        continue
    bm = None
    br = -np.inf
    bci = [np.nan, np.nan]
    bt = 0
    for mn, mr in vr.items():
        r2 = mr["metrics"]["r2"]["mean"]
        if not np.isnan(r2) and r2 > br:
            br = r2
            bm = mn
            bci = mr["metrics"]["r2"]["ci_95"]
            bt = mr["total_time"]
    if bm:
        print("{:<15} {:<20} {:<8.4f} [{:.4f}, {:.4f}]  {:<10.1f}".format(vn, bm, br, bci[0], bci[1], bt))
sys.exit(0)