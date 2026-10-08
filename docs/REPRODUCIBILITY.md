# Reproducibility Guide — HWIN-Bench v1.0

Step-by-step instructions to exactly reproduce the canonical HWIN-Bench v1.0 benchmark results.

## Prerequisites

### System Requirements
- **OS**: Linux, macOS, or Windows (WSL2 recommended on Windows)
- **Python**: 3.11 or 3.12
- **RAM**: 16 GB minimum (32 GB recommended for full GRQA)
- **Disk**: 20 GB free space
- **CPU**: 8+ cores (benchmark uses `n_jobs=-1` for ensemble models)

### Software Environment

```bash
# Create conda environment (recommended)
conda env create -f environment.yml
conda activate hwin-bench

# Or with pip (dependency spec)
pip install -r code/requirements/requirements.txt

# Verify dependencies
python -c "import numpy, pandas, sklearn, scipy; print('dependencies OK')"
```

HWIN-Bench is a research repository — the runner and validator are executed
directly (`python benchmark/...`, `python code/...`); there is no
`hwin_bench` package to install.

## Exact Reproduction Steps

### 1. Verify Data Integrity

```bash
cd HWIN-Bench

# Check all harmonized datasets present
ls data/harmonized/
# Must show 5 directories: HWIN-GRQA-V1-4, HWIN-WQP-SFBAY, HWIN-STORET-CA, HWIN-STORET-TX, HWIN-STORET-RI

# Verify checksums
python code/requirements/verify_checksums.py --quiet
# All must report OK (Linux alternative: sha256sum -c data/manifests/checksums.sha256)

# Verify key dataset properties
python -c "
import pandas as pd
obs = pd.read_csv('harmonized/HWIN-GRQA-V1-4/observations.csv')
print(f'GRQA observations: {len(obs)}')
print(f'GRQA variables: {obs.canonical_variable_id.nunique()}')
print(f'GRQA stations: {obs.station_id.nunique()}')
vars = pd.read_csv('harmonized/HWIN-GRQA-V1-4/variables.csv')
print(f'Benchmarkable vars (MIN_SAMPLES>=100): {len(vars)}')
"
```

**Note**: GRQA `observations.csv` (5.7 GB) is not included in the GitHub repository due to GitHub's 2 GB LFS file size limit. Download from Zenodo or use the smoke test for quick validation.

### 2. Run Canonical Benchmark

**This is the ONLY command for canonical reproduction** (paths may be passed
via CLI or the `HWIN_DATA_PATH` / `HWIN_OUTPUT_DIR` environment variables):

```bash
python benchmark/run_full_benchmark_fixed.py \
  --data <path-to>/HWIN-GRQA-V1-4/observations.csv \
  --output-dir output/benchmark_results/grqa_full_final_groupkfold
```

**Expected execution:**
- Wall-clock time: ~15.5 hours (932 min) on 8-core CPU
- Aggregate model training time: ~8.8 hours (528 min)
- Output directory: `output/benchmark_results/grqa_full_final_groupkfold/`
- Main result file: `GRQA_full_benchmark_complete.json`
- Per-variable results: `HWIN-VAR-XXX_results.json`

**Do NOT:**
- Modify `run_full_benchmark_fixed.py`
- Change any protocol parameters
- Use any other script
- Modify seeds, splits, models, or metrics

### 3. Verify Output

```bash
# Check result file exists and has correct structure
ls ../output/benchmark_results/grqa_full_final_groupkfold/

# Verify key metrics present
python -c "
import json
with open('output/benchmark_results/grqa_full_final_groupkfold/GRQA_full_benchmark_complete.json') as f:
    results = json.load(f)
print(f'Variables: {len(results)}')
for var_id, var_results in list(results.items())[:3]:
    print(f'  {var_id}: {len(var_results)} models')
    for model_name, model_results in list(var_results.items())[:2]:
        metrics = model_results['metrics']
        print(f'    {model_name}: R²={metrics[\"r2\"][\"mean\"]:.4f}, RMSE={metrics[\"rmse\"][\"mean\"]:.4f}')
"
```

### 4. Compare with Canonical Results

The canonical execution produced these reference results (stored in `benchmark/results/`):

| Variable | Best Model | R² (mean) | 95% CI (corrected, n=5) | RMSE (mean) |
|----------|------------|-----------|--------------------------|-------------|
| Water Temperature | Extra Trees | 0.6048 | [0.424, 0.786] | 6.586 |
| pH | Gradient Boosting | 0.0278 | [-0.078, 0.134] | 0.454 |
| Dissolved Oxygen | Ridge | 0.1575 | [0.052, 0.263] | 1.997 |
| Nitrate Nitrogen | Random Forest | 0.3293 | [0.257, 0.402] | 0.839 |
| Ammonium Nitrogen | Ridge | 0.0011 | [-0.002, 0.004] | 0.392 |
| Phosphate Phosphorus | Linear Regression | 0.0026 | [-0.001, 0.007] | 0.399 |
| DO Percent Saturation | Linear Regression | 0.0008 | [-0.001, 0.002] | 17.820 |
| Total Suspended Solids | Linear Regression | 0.0005 | [-0.000, 0.001] | 187.242 |
| Total Nitrogen | Gradient Boosting | 0.0216 | [-0.103, 0.146] | 1.969 |
| Total Ammonia Nitrogen | Lasso | 0.0042 | [0.001, 0.007] | 0.718 |
| Nitrite Nitrogen | Random Forest | 0.1703 | [0.082, 0.258] | 0.057 |

**All confidence intervals are CORRECTED** to use n=5 (5 unique GroupKFold partitions), df=4, t=2.776. Original intervals used n=25 (df=24) and were approximately 3× too narrow.

Full results: `benchmark/results/grqa_full_final_groupkfold/GRQA_full_benchmark_complete.json`
Per-variable: `benchmark/results/grqa_full_final_groupkfold/HWIN-VAR-XXX.json`
Statistical tests: Reserved for v1.1+ (not executed in v1.0)  
Certification: `benchmark/reproducibility/CANONICAL_EXECUTION_CERTIFICATE.md`

## Protocol Compliance Checklist

The frozen protocol (`benchmark/protocol/01_HWIN_BENCH_PROTOCOL_v1.0.md`) requires:

- [ ] **Data**: GRQA v1.4 only for regression benchmark (11 benchmark variables, MIN_SAMPLES=100)
- [ ] **Sampling**: MAX_SAMPLES=200,000, random_state=42
- [ ] **Features**: Exactly 7 features (lat, lon, year, month, doy, sin_doy, cos_doy)
- [ ] **Splits**: 5 unique GroupKFold partitions by station_id, 5 deterministic repetitions with seeds [42, 123, 256, 512, 1024]
- [ ] **Models**: Exactly 7 classical sklearn models with specified hyperparameters
- [ ] **Metrics**: MAE, RMSE, R², MAPE, MedAE
- [ ] **CI**: 95% t-distribution on 5 unique GroupKFold partitions (n=5, df=4, t=2.776)
- [ ] **Output**: JSON format per protocol §11
- [ ] **Statistical testing**: Reserved for v1.1+ (Kruskal-Wallis, Wilcoxon, Cliff's Delta, Holm-Bonferroni NOT executed in v1.0)

**Any deviation = protocol violation.**

## Troubleshooting Reproduction

### Results Don't Match

| Issue | Check |
|-------|-------|
| Different R² values | Verify GRQA version (must be v1.4 from Zenodo 15335450) |
| Different fold counts | Verify GroupKFold by station_id (not random split) |
| Missing variables | Verify MIN_SAMPLES=100 filter applied after harmonization |
| Memory errors | Reduce n_jobs for RF/ET/GB; use chunked processing |

### Common Protocol Violations

| Violation | Consequence |
|-----------|-------------|
| Using `run_full_benchmark.py` (legacy) | Results invalid |
| Changing seeds | Results not comparable |
| Adding XGBoost/LightGBM | Not in v1.0 scope |
| Omitting Holm-Bonferroni | Not executed in v1.0 (reserved for v1.1+) |
| Reporting FAIR numeric scores | Protocol requires qualitative only |

### Environment Issues

```bash
# Check sklearn version (must match canonical)
python -c "import sklearn; print(sklearn.__version__)"
# Canonical: 1.5.x

# Check numpy/pandas
python -c "import numpy, pandas; print(numpy.__version__, pandas.__version__)"
```

## Smoke Test (Quick Validation)

For CI/CD or quick checks:

```bash
cd benchmark
python run_full_benchmark_fixed.py --smoke-test
# Runs 1 variable × 1 model × 1 fold in ~30 seconds
# Validates pipeline integrity without full compute
```

## Transfer Learning Reproduction

Transfer learning (protocol §16) is **not** part of the canonical regression benchmark. To reproduce transfer experiments:

```bash
# After fixing NaN bug (see COMP-004 fix)
python benchmark/run_transfer_experiments.py
```

## Computational Reproducibility

### Random Seeds (All Fixed)

| Component | Seeds |
|-----------|-------|
| Benchmark GroupKFold | [42, 123, 256, 512, 1024] |
| Data Sampling (200K cap) | 42 |
| Model Training | 42 (per model) |
| hwin-baselines | [42, 123, 256, 512, 1024] (external repo) |
| hwin-net | [42, 123, 456, 789, 999] (external repo) |

### Hardware Independence

Results should be bitwise reproducible across hardware for:
- Linear models (deterministic)
- Ridge/Lasso/ElasticNet (deterministic with fixed random_state)

Results may vary slightly (±0.001) for:
- Random Forest / Extra Trees / Gradient Boosting (parallel execution order)

This is expected and within statistical uncertainty.

## Certification

The canonical execution was certified on 2026-07-24:

- **Certificate**: `benchmark/reproducibility/CANONICAL_EXECUTION_CERTIFICATE.md`
- **Execution log**: `EXECUTION_LOG.md`
- **Reproducibility verification**: `REPRODUCIBILITY_VERIFICATION.md`

Your reproduction is successful if:
1. All 1,925 model fits complete
2. Output structure matches protocol §11
3. Key metrics fall within 95% CI of canonical results
4. No protocol violations detected

## Support

- **Issues**: GitHub Issues with `reproduction` label
- **Protocol questions**: Reference `benchmark/protocol/01_HWIN_BENCH_PROTOCOL_v1.0.md` section numbers
- **Data issues**: Check `docs/DATA_GUIDE.md` and `docs/DATA_DICTIONARY.md`

---

**Remember**: The protocol is frozen. If you need different parameters, that's HWIN-Bench v1.1+.