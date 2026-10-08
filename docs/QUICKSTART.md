# Quickstart Guide — HWIN-Bench v1.0

Get up and running in 5 minutes.

## Prerequisites

- Python 3.11+
- 8+ GB RAM (16 GB recommended for full benchmark)
- 10 GB free disk space
- Git

## 1. Clone & Install

HWIN-Bench is a research repository — scripts run directly, no package install.

```bash
git clone https://github.com/Zakariya-Q/HWIN-Bench.git
cd HWIN-Bench

# Using conda (recommended)
conda env create -f environment.yml
conda activate hwin-bench

# Or using pip (dependency spec)
pip install -r code/requirements/requirements.txt
```

## 2. Verify Data

```bash
# Check that harmonized data is present
ls data/harmonized/
# Should show: HWIN-GRQA-V1-4/  HWIN-WQP-SFBAY/  HWIN-STORET-CA/  HWIN-STORET-TX/  HWIN-STORET-RI/

# Verify checksums (from the repository root; cross-platform)
python code/requirements/verify_checksums.py --quiet
# On Linux, sha256sum -c data/manifests/checksums.sha256 also works
```

## 3. Run Smoke Test (30 seconds)

```bash
# No download needed — runs on the in-repo STORET-RI dataset
python benchmark/run_full_benchmark_fixed.py \
  --data data/harmonized/HWIN-STORET-RI/observations.csv \
  --output-dir output/smoke_results \
  --smoke-test
```

Expected output: Quick validation on 1 variable × 1 model × 1 fold.

## 4. Run Full Benchmark (5-6 hours)

```bash
cd benchmark
python run_full_benchmark_fixed.py \
  --data <path-to>/HWIN-GRQA-V1-4/observations.csv \
  --output-dir ../output/benchmark_results/grqa_recomputation
```

This executes the **frozen protocol**:
- 11 benchmark variables × 7 models × 5 unique GroupKFold partitions × 5 deterministic repetitions = 1,925 historical fits (385 unique evaluations)
- GroupKFold by station_id
- Seeds: [42, 123, 256, 512, 1024] (5 deterministic repetitions of the fixed partition set)
- Output: `all_results.json` + per-variable `HWIN-VAR-XXX_results.json` (schema of the shipped canonical results)

## 5. Inspect Results

```bash
# Canonical reference results are shipped in the repo:
cat benchmark/results/grqa_recomputation/all_results.json | jq '.'

# Or use the analysis notebook
jupyter lab examples/quickstart/analyze_results.ipynb
```

## Key Files

| File | Purpose |
|------|---------|
| `benchmark/protocol/01_HWIN_BENCH_PROTOCOL_v1.0.md` | Frozen protocol (immutable) |
| `benchmark/run_full_benchmark_fixed.py` | Canonical benchmark runner |
| `data/harmonized/HWIN-GRQA-V1-4/observations.csv` | Primary benchmark data (note: GRQA observations.csv is in Zenodo) |
| `ontology/canonical_variable_ontology.csv` | 49 canonical variables |
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
| `ModuleNotFoundError` | Ensure the conda env is active, or run `pip install -r code/requirements/requirements.txt` |
| Data not found | Check `data/harmonized/` exists; re-run checksum verification |
| Memory error | Reduce `n_jobs` in RandomForest/ExtraTrees/GradientBoosting |
| Protocol violation | Do not modify `run_full_benchmark_fixed.py` or protocol parameters |

---

**Need help?** Open a GitHub Issue or see `docs/REPRODUCIBILITY.md`.