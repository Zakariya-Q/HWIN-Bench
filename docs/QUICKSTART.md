# Quickstart Guide — HWIN-Bench v1.0

Get up and running in 5 minutes.

## Prerequisites

- Python 3.11+
- 8+ GB RAM (16 GB recommended for full benchmark)
- 10 GB free disk space
- Git

## 1. Clone & Install

```bash
git clone https://github.com/HWIN-Bench/HWIN-Bench-v1.0.git
cd HWIN-Bench-v1.0

# Using conda (recommended)
conda env create -f environment.yml
conda activate hwin-bench

# Or using pip
pip install -r requirements.txt
pip install -e .
```

## 2. Verify Data

```bash
# Check that harmonized data is present
ls data/harmonized/
# Should show: HWIN-GRQA-V1-4/  HWIN-WQP-SFBAY/  HWIN-STORET-CA/  HWIN-STORET-TX/  HWIN-STORET-RI/

# Verify checksums
cd data/
sha256sum -c manifests/checksums.sha256
```

## 3. Run Smoke Test (30 seconds)

```bash
cd code/benchmark
python run_full_benchmark_fixed.py --smoke-test
```

Expected output: Quick validation on 1 variable × 1 model × 1 fold.

## 4. Run Full Benchmark (5-6 hours)

```bash
cd code/benchmark
python run_full_benchmark_fixed.py
```

This executes the **frozen protocol**:
- 11 benchmark variables × 7 models × 5 seeds × 5 folds = 2,275 model fits
- GroupKFold by station_id
- Seeds: [42, 123, 256, 512, 1024]
- Output: `../../output/benchmark_results/grqa_full_final_groupkfold/GRQA_full_benchmark_complete.json`

## 5. Inspect Results

```bash
# View aggregated results
cat ../../output/benchmark_results/grqa_full_final_groupkfold/GRQA_full_benchmark_complete.json | jq '.'

# Or use the analysis notebook
jupyter lab examples/quickstart/analyze_results.ipynb
```

## Key Files

| File | Purpose |
|------|---------|
| `benchmark/protocol/01_HWIN_BENCH_PROTOCOL_v1.0.md` | Frozen protocol (immutable) |
| `code/benchmark/run_full_benchmark_fixed.py` | Canonical benchmark runner |
| `data/harmonized/HWIN-GRQA-V1-4/observations.csv` | Primary benchmark data |
| `ontology/canonical_variable_ontology.csv` | 51 canonical variables |
| `ontology/variable_synonym_dictionary.csv` | 89 source→canonical mappings |
| `ontology/unit_harmonization_rules.csv` | 92 unit conversion rules |

## Next Steps

- Read `docs/DATA_GUIDE.md` for complete data documentation
- Read `docs/REPRODUCIBILITY.md` for exact reproduction steps
- Read `docs/LIMITATIONS.md` for scope and known issues
- See `examples/quickstart/` for download and analysis scripts

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError` | Run `pip install -e .` from repo root |
| Data not found | Check `data/harmonized/` exists; re-run checksum verification |
| Memory error | Reduce `n_jobs` in RandomForest/ExtraTrees/GradientBoosting |
| Protocol violation | Do not modify `run_full_benchmark_fixed.py` or protocol parameters |

---

**Need help?** Open a GitHub Issue or see `docs/REPRODUCIBILITY.md`.