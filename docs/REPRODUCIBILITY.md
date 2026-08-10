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
# Create conda environment
conda env create -f environment.yml
conda activate hwin-bench

# Or with pip
pip install -r requirements.txt
pip install -e .

# Verify installation
python -c "import hwin_bench; print(hwin_bench.__version__)"
```

## Exact Reproduction Steps

### 1. Verify Data Integrity

```bash
cd HWIN_Bench_v1_RELEASE

# Check all harmonized datasets present
ls data/harmonized/
# Must show 5 directories: HWIN-GRQA-V1-4, HWIN-WQP-SFBAY, HWIN-STORET-CA, HWIN-STORET-TX, HWIN-STORET-RI

# Verify checksums
cd data/
sha256sum -c manifests/checksums.sha256
# All must report OK

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

### 2. Run Canonical Benchmark

**This is the ONLY command for canonical reproduction:**

```bash
cd benchmark
python run_full_benchmark_fixed.py
```

**Expected execution:**
- Runtime: ~5-6 hours on 8-core CPU
- Output directory: `../output/benchmark_results/grqa_full_final_groupkfold/`
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
with open('../output/benchmark_results/grqa_full_final_groupkfold/GRQA_full_benchmark_complete.json') as f:
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

| Variable | Best Model | R² (mean) | RMSE (mean) |
|----------|------------|-----------|-------------|
| HWIN-VAR-001 (Temp) | Gradient Boosting | ~0.89 | ~1.23 |
| HWIN-VAR-002 (pH) | Random Forest | ~0.67 | ~0.34 |
| HWIN-VAR-003 (DO) | Extra Trees | ~0.71 | ~0.89 |
| HWIN-VAR-008 (NO3-N) | Gradient Boosting | ~0.78 | ~0.45 |
| HWIN-VAR-010 (PO4-P) | Random Forest | ~0.65 | ~0.023 |

**Acceptance criteria**: Your results should match within statistical uncertainty (95% CI overlap).

## Protocol Compliance Checklist

The frozen protocol (`benchmark/protocol/01_HWIN_BENCH_PROTOCOL_v1.0.md`) requires:

- [ ] **Data**: GRQA v1.4 only for regression benchmark (11 benchmark variables, MIN_SAMPLES=100)
- [ ] **Sampling**: MAX_SAMPLES=200,000, random_state=42
- [ ] **Features**: Exactly 7 features (lat, lon, year, month, doy, sin_doy, cos_doy)
- [ ] **Splits**: 5×5 GroupKFold by station_id, seeds [42, 123, 256, 512, 1024]
- [ ] **Models**: Exactly 7 classical sklearn models with specified hyperparameters
- [ ] **Metrics**: MAE, RMSE, R², MAPE, MedAE
- [ ] **Statistics**: Kruskal-Wallis, Wilcoxon, Cliff's Delta, Holm-Bonferroni
- [ ] **CI**: 95% t-distribution on 5 unique GroupKFold partitions × 5 deterministic repetitions means
- [ ] **Output**: JSON format per protocol §11

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
| Omitting Holm-Bonferroni | Statistical claims invalid |
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
1. All 2,275 model fits complete
2. Output structure matches protocol §11
3. Key metrics fall within 95% CI of canonical results
4. No protocol violations detected

## Support

- **Issues**: GitHub Issues with `reproduction` label
- **Protocol questions**: Reference `benchmark/protocol/01_HWIN_BENCH_PROTOCOL_v1.0.md` section numbers
- **Data issues**: Check `docs/DATA_GUIDE.md` and `docs/DATA_DICTIONARY.md`

---

**Remember**: The protocol is frozen. If you need different parameters, that's HWIN-Bench v1.1+.