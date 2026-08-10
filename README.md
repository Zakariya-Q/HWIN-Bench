# HWIN-Bench v1.0 — Public Release

**Heterogeneous Water Quality Intelligence Benchmark — Version 1.0**

[![DOI](https://img.shields.io/badge/DOI-10.5281/zenodo.XXXXXXX-blue)](https://doi.org/10.5281/zenodo.XXXXXXX)
[![License](https://img.shields.io/badge/License-CC--BY--4.0-green)](LICENSE)
[![Protocol](https://img.shields.io/badge/Protocol-FROZEN%20v1.0-red)](benchmark/protocol/01_HWIN_BENCH_PROTOCOL_v1.0.md)
[![Reproducibility](https://img.shields.io/badge/Reproducibility-CERTIFIED-brightgreen)](benchmark/reproducibility/)

---

## What is HWIN-Bench?

HWIN-Bench (Heterogeneous Water quality Intelligence Benchmark) is a **curated, reproducible benchmark suite** for evaluating machine learning models on real-world water quality prediction tasks. It addresses a critical gap: most ML benchmarks use synthetic or homogeneous data, while environmental water quality data is inherently heterogeneous — multi-source, multi-scale, sparse, and noisy.

**HWIN-Bench v1.0** provides:
- **5 canonical datasets** harmonized to a common schema (Canonical Benchmark Schema - CBS)
- **49-variable ontology** (Canonical Variable Ontology - CVO) with 89 cross-dataset synonym mappings
- **Frozen benchmark protocol** (v1.0) specifying every computational parameter
- **11 benchmarkable water quality variables** on the Global River Quality Archive (GRQA v1.4)
- **7 classical ML models** evaluated via 5 unique GroupKFold partitions × 5 deterministic repetitions (1,925 historical fits)
- **Full statistical rigor**: Kruskal-Wallis, Wilcoxon signed-rank, Cliff's Delta, Holm-Bonferroni correction
- **Certified reproducibility**: Canonical execution completed and independently verified

---

## Why Does HWIN-Bench Exist?

Water quality modeling is essential for environmental management, public health, and climate adaptation. Yet ML research on water quality suffers from:
1. **No standard benchmark** — each paper uses different data, splits, metrics
2. **Data heterogeneity ignored** — models tested on clean subsets, not real-world messiness
3. **Reproducibility crisis** — results cannot be verified or compared
4. **Transfer learning untested** — can models trained on global data predict in data-scarce regions?

HWIN-Bench solves this by providing a **single, frozen, immutable benchmark protocol** that any researcher can execute and verify.

---

## The Five Canonical Datasets

| Dataset ID | Name | Provider | Version | License | Raw Redistributable | Size (Raw) |
|------------|------|----------|---------|---------|---------------------|------------|
| **HWIN-GRQA-V1-4** | Global River Quality Archive | Virro et al. (ESSD) | 1.4 | CC-BY-4.0 | ✅ YES | 6.0 GB |
| **HWIN-WQP-SFBAY** | USGS/EPA WQP — San Francisco Bay | USGS / EPA | 2024 | Public Domain (17 USC 105) | ✅ YES | 4.6 MB |
| **HWIN-STORET-CA** | EPA STORET — California | US EPA | 2024.1 | Public Domain (17 USC 105) | ✅ YES | 42.7 MB |
| **HWIN-STORET-TX** | EPA STORET — Texas | US EPA | 2024.1 | Public Domain (17 USC 105) | ✅ YES | 46.5 MB |
| **HWIN-STORET-RI** | EPA STORET — Rhode Island | US EPA | 2024.1 | Public Domain (17 USC 105) | ✅ YES | 0.5 MB |

### Data Redistribution Policy

**All five datasets CAN be redistributed in raw form** through this GitHub repository (and Zenodo):

- **GRQA v1.4**: Licensed CC-BY-4.0 by the authors (Zenodo record [15335450](https://zenodo.org/records/15335450)). Redistribution permitted with attribution.
- **WQP / STORET (CA, TX, RI)**: US Government works (USGS NWIS + EPA STORET/WQX) — **public domain** under 17 USC §105. No copyright restrictions.

**However**, to respect original providers and ensure users get the latest versions:
- This release includes the **HWIN-Bench harmonized (CBS) versions** of all datasets
- Raw source data is also included where licenses permit (all 5 datasets)
- Users are encouraged to download fresh copies from original providers for production use
- See `data/README.md` for download instructions and checksums

---

## Harmonized Variables

HWIN-Bench maps 100+ source variable names across 5 datasets to **49 canonical variables** (HWIN-VAR-001 through HWIN-VAR-049). The **11 benchmarkable variables** (meeting MIN_SAMPLES ≥ 100 in GRQA) are:

| Variable ID | Canonical Name | GRQA Observations |
|-------------|----------------|-------------------|
| HWIN-VAR-001 | Water Temperature | 5,508,690 |
| HWIN-VAR-002 | pH | 4,702,926 |
| HWIN-VAR-003 | Dissolved Oxygen | 2,758,590 |
| HWIN-VAR-004 | Turbidity | ≥100 |
| HWIN-VAR-005 | Specific Conductance | ≥100 |
| HWIN-VAR-008 | Nitrate Nitrogen | 2,343,593 |
| HWIN-VAR-009 | Ammonium Nitrogen | 999,283 |
| HWIN-VAR-010 | Phosphate Phosphorus | 2,858,114 |
| HWIN-VAR-014 | DO Percent Saturation | 1,690,075 |
| HWIN-VAR-015 | Total Suspended Solids | 1,308,520 |
| HWIN-VAR-022 | Biochemical Oxygen Demand | ≥100 |
| HWIN-VAR-023 | Chemical Oxygen Demand | 119,220 |
| HWIN-VAR-033 | Nitrite Nitrogen | 1,310,136 |

Full ontology: `ontology/canonical_variable_ontology.csv`  
Synonym dictionary: `ontology/variable_synonym_dictionary.csv` (89 mappings)  
Unit harmonization: `ontology/unit_harmonization_rules.csv` (92 rules)

---

## Installation

```bash
# Clone the repository
git clone https://github.com/HWIN-Bench/HWIN-Bench-v1.0.git
cd HWIN-Bench-v1.0

# Create environment (Python 3.11+)
conda env create -f environment.yml
conda activate hwin-bench

# Or with pip
pip install -r requirements.txt

# Install HWIN-Bench package
pip install -e .
```

---

## Obtaining the Data

### Option 1: Use Included Harmonized Data (Recommended for Reproducibility)

The `data/harmonized/` directory contains all 5 datasets in the **Canonical Benchmark Schema (CBS)** format — ready for benchmark execution.

```bash
# Verify checksums
cd data/harmonized
sha256sum -c manifests/checksums.sha256
```

### Option 2: Download Fresh from Original Providers

For production use, download the latest versions:

| Dataset | Source | Command |
|---------|--------|---------|
| GRQA v1.4 | Zenodo | `wget https://zenodo.org/records/15335450/files/GRQA_data_v1.4.zip` |
| WQP SF Bay | Water Quality Portal | Use WQP API (see `examples/quickstart/download_wqp.py`) |
| STORET CA/TX/RI | EPA WQP | Use WQP API with state filters |

**Exact versions required for HWIN-Bench v1.0 reproduction:**
- GRQA: v1.4 (DOI: 10.5281/zenodo.15335450)
- WQP/STORET: As accessed 2026-07-08 (documented in dataset metadata)

### Option 3: Run the Canonical Pipeline

```bash
# Full canonical pipeline: download → harmonize → validate → benchmark
python -m hwin_bench.cli pipeline --all
```

---

## Reproducing the Benchmark

### Quick Smoke Test (5 minutes)
```bash
cd HWIN_Bench_v1_RELEASE
python benchmark/run_full_benchmark_fixed.py --smoke-test
```

### Full Canonical Benchmark (5-6 hours on CPU)
```bash
cd HWIN_Bench_v1_RELEASE
python benchmark/run_full_benchmark_fixed.py
```

**Expected output**: `output/benchmark_results/grqa_full_final_groupkfold/GRQA_full_benchmark_complete.json`

### Protocol Compliance
The frozen protocol (`benchmark/protocol/01_HWIN_BENCH_PROTOCOL_v1.0.md`) specifies:
- **Data**: GRQA v1.4, 11 variables, MAX_SAMPLES=200,000, MIN_SAMPLES=100
- **Features**: 7 (lat, lon, year, month, day_of_year, sin_doy, cos_doy)
- **Splits**: 5 unique GroupKFold partitions by station_id, 5 deterministic repetitions with seeds [42, 123, 256, 512, 1024]
- **Models**: 7 classical (Linear, Ridge, Lasso, ElasticNet, RF, ExtraTrees, GradientBoosting)
- **Metrics**: MAE, RMSE, R², MAPE, MedAE
- **Statistics**: Kruskal-Wallis, Wilcoxon, Cliff's Delta, Holm-Bonferroni

**Any deviation is a protocol violation.**

---

## Canonical Results

The certified canonical execution produced results for 11 variables × 7 models across 5 unique GroupKFold partitions × 5 deterministic repetitions (1,925 historical fits). Summary:

| Variable | Best Model | Best R² (mean) | Best RMSE (mean) |
|----------|------------|----------------|------------------|
| Water Temperature | Gradient Boosting | 0.89 | 1.23 °C |
| pH | Random Forest | 0.67 | 0.34 |
| Dissolved Oxygen | Extra Trees | 0.71 | 0.89 mg/L |
| ... | ... | ... | ... |

Full results: `benchmark/results/GRQA_full_benchmark_complete.json`  
Per-variable: `benchmark/results/HWIN-VAR-XXX_results.json`  
Statistical tests: `benchmark/results/statistical_test_results.json`  
Certification: `benchmark/reproducibility/CANONICAL_EXECUTION_CERTIFICATE.md`

---

## Citation

If you use HWIN-Bench, please cite:

```bibtex
@software{hwin_bench_v1,
  title = {HWIN-Bench v1.0: Heterogeneous Water Quality Intelligence Benchmark},
  author = {HWIN-Bench Consortium},
  year = {2026},
  version = {1.0.0},
  doi = {10.5281/zenodo.XXXXXXX},
  url = {https://github.com/HWIN-Bench/HWIN-Bench-v1.0}
}
```

Dataset citations (required when using individual datasets):

1. **GRQA v1.4**: Virro, H., Amatulli, G., Kmoch, A., Shen, L., & Uuemaa, E. (2025). *Global River Water Quality Archive (GRQA) (Version 1.4)* [Dataset]. Zenodo. https://doi.org/10.5281/zenodo.15335450

2. **WQP/STORET**: U.S. Geological Survey and Environmental Protection Agency. *Water Quality Portal*. Retrieved [date] from https://www.waterqualitydata.us/

See `CITATION.cff` for machine-readable citation metadata.

---

## Dataset Licenses

| Dataset | License | Attribution Required |
|---------|---------|---------------------|
| GRQA v1.4 | CC-BY-4.0 | Yes — see `licenses/ATTRIBUTION.md` |
| WQP/STORET | Public Domain | No legal requirement; recommended attribution in `licenses/ATTRIBUTION.md` |

Full license audit: `licenses/DATASET_LICENSE_AUDIT.csv`  
Attribution details: `licenses/ATTRIBUTION.md`

---

## Limitations

1. **GRQA-only regression benchmark**: Only GRQA v1.4 is used for the canonical regression benchmark (protocol §3.3). STORET/WQP datasets are for transfer learning evaluation (protocol §16).

2. **Classical ML only**: v1.0 includes 7 sklearn models. Deep learning (HWIN-Net), XGBoost, LightGBM, CatBoost are reserved for v1.1+.

3. **MAX_SAMPLES cap**: 200,000 observations per variable (12 of 11 variables affected). This is a computational constraint, not a scientific decision.

4. **Spatial/temporal bias**: GRQA overrepresents Europe/North America; tropical/southern hemisphere underrepresented.

5. **No causal claims**: Benchmark measures predictive performance, not causal mechanisms.

6. **Transfer learning NaN bug**: Known issue in transfer evaluation (protocol §16) — must be fixed before v1.1.

Full limitations: `docs/LIMITATIONS.md`

---

## Documentation

| Document | Description |
|----------|-------------|
| `docs/QUICKSTART.md` | 5-minute quickstart guide |
| `docs/DATA_GUIDE.md` | Complete data access and format guide |
| `docs/DATA_DICTIONARY.md` | Variable and column definitions |
| `docs/REPRODUCIBILITY.md` | Step-by-step reproduction instructions |
| `docs/LIMITATIONS.md` | Known limitations and scope |
| `docs/DATA_PROVENANCE.md` | Full provenance chains for all datasets |
| `benchmark/protocol/01_HWIN_BENCH_PROTOCOL_v1.0.md` | Frozen benchmark protocol (immutable) |

---

## License

HWIN-Bench v1.0 code, protocol, and documentation: **CC-BY-4.0** (see `LICENSE`)

Individual datasets retain their original licenses (see table above).

---

## Contact & Contributing

- **Issues**: GitHub Issues for bug reports and questions
- **Discussions**: GitHub Discussions for methodology questions
- **Email**: hwin-bench@[domain].org

See `CONTRIBUTING.md` for contribution guidelines.

---

**HWIN-Bench v1.0 — Making water quality ML rigorous, reproducible, and comparable.**