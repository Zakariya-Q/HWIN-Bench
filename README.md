# HWIN-Bench v1.0 — Public Release

**Heterogeneous Water Quality Intelligence Benchmark — Version 1.0**

> **Versioning**: HWIN-Bench **v1.0** is the frozen scientific benchmark and
> protocol (results, variables, models, splits, and metrics are immutable).
> Repository maintenance releases (1.0.1, 1.0.2, …) fix packaging,
> documentation, and infrastructure without touching the scientific content.
> Current maintenance release: **1.0.4** (see `CHANGELOG.md`).

[![License](https://img.shields.io/badge/License-CC--BY--4.0-green)](LICENSE)
[![Protocol](https://img.shields.io/badge/Protocol-FROZEN%20v1.0-red)](benchmark/protocol/01_HWIN_BENCH_PROTOCOL_v1.0.md)
[![Reproducibility](https://img.shields.io/badge/Reproducibility-CERTIFIED-brightgreen)](benchmark/reproducibility/)
[![Release](https://img.shields.io/github/v/release/Zakariya-Q/HWIN-Bench)](https://github.com/Zakariya-Q/HWIN-Bench/releases/tag/v1.0.4)

---

## What is HWIN-Bench?

HWIN-Bench (Heterogeneous Water quality Intelligence Benchmark) is a **curated, reproducible benchmark suite** for evaluating machine learning models on real-world water quality prediction tasks. It addresses a critical gap: most ML benchmarks use synthetic or homogeneous data, while environmental water quality data is inherently heterogeneous — multi-source, multi-scale, sparse, and noisy.

**HWIN-Bench v1.0** provides:

- **Five harmonized dataset collections**, with dataset-specific data-quality findings documented in `docs/DATA_QUALITY_VALIDATION_REPORT.md`
- **49-variable ontology** (Canonical Variable Ontology - CVO) with 89 cross-dataset synonym mappings
- **Versioned v1.0 protocol and released result artifacts**; the protocol's stated variable scope and the 11 variables in the canonical result bundle are not yet reconciled
- **11 variables** represented in the current canonical regression result artifacts for GRQA v1.4
- **7 classical ML models** evaluated via 5 unique GroupKFold partitions × 5 deterministic repetitions (1,925 historical fits)
- **Corrected confidence intervals** (n=5, df=4) — all CIs ~3× wider than originally reported
- Canonical execution artifacts and verification records are included in the repository

---

## Why Does HWIN-Bench Exist?

Water quality modeling is essential for environmental management, public health, and climate adaptation. Yet ML research on water quality suffers from:

1. **No standard benchmark** — each paper uses different data, splits, metrics
2. **Data heterogeneity ignored** — models tested on clean subsets, not real-world messiness
3. **Reproducibility crisis** — results cannot be verified or compared
4. **Transfer learning untested** — can models trained on global data predict in data-scarce regions?

HWIN-Bench solves this by providing a **single, frozen, immutable benchmark protocol** that any researcher can execute and verify.

---

## The Five Dataset Collections

Dataset counts below describe the current harmonized files, not total records held by the upstream providers. Observation rows exclude the CSV header; station counts are distinct station IDs represented in the observation rows; variable counts are data rows in each `variables.csv` catalogue.

| Dataset ID | Observation rows | Distinct station IDs in observations | Variable catalogue rows | Distribution and status |
|---|---:|---:|---:|---|
| **HWIN-GRQA-V1-4** | 25,850,907 | 107,828 | 13 | Observations are provided as ten byte-chunks in [GitHub Release v1.0.4](https://github.com/Zakariya-Q/HWIN-Bench/releases/tag/v1.0.4); 11 variables appear in the canonical benchmark results |
| **HWIN-WQP-SFBAY** | 51,050 | 642 | 18 | Included in `data/harmonized/`; reduced 8-column observations schema; does not fully pass strict CBS validation |
| **HWIN-STORET-CA** | 172,103 | 48,338 | 22 | Included in `data/harmonized/`; does not fully pass strict CBS validation |
| **HWIN-STORET-TX** | 210,614 | 4,988 | 22 | Included in `data/harmonized/`; does not fully pass strict CBS validation |
| **HWIN-STORET-RI** | 2,294 | 95 | 19 | Included in `data/harmonized/`; does not fully pass strict CBS validation |

Counts are based on the current audit and the report at `docs/DATA_QUALITY_VALIDATION_REPORT.md`; do not reuse the older rounded counts in historical audit inventories. The four regional datasets have known strict-CBS validation failures. Their presence in the repository is not a statement that they are fully CBS-compliant.

### Source and redistribution notes

- **GRQA v1.4** is an upstream dataset with a CC-BY-4.0 attribution requirement. The GitHub Release contains the HWIN-Bench harmonized benchmark input; downloading the original GRQA archive alone does not reproduce this exact derived CSV.
- **Water Quality Portal / STORET / WQX** includes records from multiple contributing agencies. Do not label the full aggregated HWIN subset as automatically public domain. Review the applicable source and contributor terms before redistributing each subset. The current source-license assessment needs source-specific review.
- The HWIN-Bench software, protocol, and documentation license does not override the licenses or terms that apply to source data.

See [`docs/DATA_AVAILABILITY.md`](docs/DATA_AVAILABILITY.md) for the authoritative release/download procedure, exact GRQA hash, repository-snapshot identity, and publication-DOI status. See [`licenses/ATTRIBUTION.md`](licenses/ATTRIBUTION.md) and [`licenses/DATASET_LICENSE_AUDIT.csv`](licenses/DATASET_LICENSE_AUDIT.csv) for data attribution and license review.

## Harmonized Variables

HWIN-Bench maps 100+ source variable names across 5 datasets to **49 canonical variables** (HWIN-VAR-001 through HWIN-VAR-049). The **11 benchmarkable variables** (meeting MIN_SAMPLES ≥ 100 in GRQA and selected for the v1.0 canonical regression benchmark) are:

| Variable ID | Canonical Name | GRQA Observations |
|-------------|----------------|-------------------|
| HWIN-VAR-001 | Water Temperature | 5,508,690 |
| HWIN-VAR-002 | pH | 4,702,926 |
| HWIN-VAR-003 | Dissolved Oxygen | 2,758,590 |
| HWIN-VAR-008 | Nitrate Nitrogen | 2,343,593 |
| HWIN-VAR-009 | Ammonium Nitrogen | 999,283 |
| HWIN-VAR-010 | Phosphate Phosphorus | 2,858,114 |
| HWIN-VAR-014 | DO Percent Saturation | 1,690,075 |
| HWIN-VAR-015 | Total Suspended Solids | 1,308,520 |
| HWIN-VAR-028 | Total Nitrogen | 1,755,110 |
| HWIN-VAR-031 | Total Ammonia Nitrogen | 615,870 |
| HWIN-VAR-033 | Nitrite Nitrogen | 1,310,136 |

**Important distinction**: HWIN-Bench v1.0 defines a **49-variable Canonical Variable Ontology (CVO)**, but the **canonical v1.0 regression benchmark** includes only **11 variables** that met all eligibility criteria (MIN_SAMPLES ≥ 100 in GRQA, valid source mappings, sufficient harmonized observations). The remaining 38 ontology variables were not included in the v1.0 regression benchmark due to insufficient harmonized GRQA observations, missing source mappings, or zero harmonized observations.

**Full ontology**: `ontology/canonical_variable_ontology.csv` (49 variables)  
**Synonym dictionary**: `ontology/variable_synonym_dictionary.csv` (89 mappings)  
**Unit harmonization**: `ontology/unit_harmonization_rules.csv` (92 rules)

---

## Installation

HWIN-Bench is a research repository — the benchmark runner and validator are
executed directly, no package installation is required.

```bash
# Clone the repository
git clone https://github.com/Zakariya-Q/HWIN-Bench.git
cd HWIN-Bench

# Create the environment (Python 3.11+)
conda env create -f environment.yml
conda activate hwin-bench

# Or with pip — dependency spec at code/requirements/requirements.txt
pip install -r code/requirements/requirements.txt
```

Runtime dependencies for the benchmark and validator: numpy, pandas,
scikit-learn, scipy (see `environment.yml` for the pinned versions used in
the certified run).

**Note**: `code/requirements/requirements.txt` lists the fuller development
dependency set from the original harmonization pipeline. The core benchmark
and validation need only numpy/pandas/scikit-learn/scipy.

---

## Obtaining the Data

### Canonical GRQA benchmark input

The full HWIN-Bench harmonized GRQA `observations.csv` is **not tracked in the repository tree**. It is published as ten byte-chunks of one gzip stream in the [v1.0.4 GitHub Release](https://github.com/Zakariya-Q/HWIN-Bench/releases/tag/v1.0.4). Use these assets for reproducing the released Run-B input; the original upstream GRQA ZIP is not a byte-identical replacement for the harmonized file.

From a Bash shell (Linux, macOS, WSL, or Git Bash) with the GitHub CLI installed:

~~~bash
mkdir -p hwin-grqa-release
gh release download v1.0.4 --repo Zakariya-Q/HWIN-Bench \
  --pattern 'hwin-grqa-v1-4_observations.csv.gz.part-*' --dir hwin-grqa-release
cat hwin-grqa-release/hwin-grqa-v1-4_observations.csv.gz.part-* | gzip -dc > observations.csv
sha256sum observations.csv
wc -l observations.csv
~~~

Expected decompressed CSV SHA-256: `989e5a6ba07499d81443c8819ef7f1e786fdef8a52661474a2bf5cc4a2ed6f8f`. The verified output is 6,016,295,802 bytes and has 25,850,908 lines including the header (25,850,907 data rows). The exact documented chunk-reassembly, gzip-integrity, size/line-count, and checksum round trip was verified during the release audit.

Place the restored file at `data/harmonized/HWIN-GRQA-V1-4/observations.csv` in a checkout of the matching release snapshot before running the full benchmark. The repository archive attached to v1.0.4 is a snapshot at commit `a70033d`; the annotated `v1.0.4` tag peels to commit `1def10f`. These are not the same tree, so use the release-asset instructions and snapshot identity documented above rather than assuming the archive exactly equals the tag tree.

### Regional dataset files

The four smaller regional observation CSVs and their station/variable metadata are present under `data/harmonized/`. Their latest measured counts and strict-CBS findings are in `docs/DATA_QUALITY_VALIDATION_REPORT.md` and `data/manifests/DATASET_RELEASE_INVENTORY.csv`.

To verify repository files from the repository root:

~~~bash
python code/requirements/verify_checksums.py
~~~

Install Git LFS before verification so LFS-tracked files are materialized and handled according to the documented checksum policy.

### Upstream source archive versus harmonized input

The original GRQA v1.4 source dataset is available from [Zenodo record 15335450](https://zenodo.org/records/15335450). Cite it as the upstream dataset. For reproducing the released HWIN-Bench benchmark, use the HWIN-Bench Release assets and expected hash above.

### Publication DOI

The HWIN-Bench deposit DOI `10.5281/zenodo.21877825` remains **reserved but unpublished** as of 2026-10-19. Do not cite it as a live DOI or use it as the current data-download route. Until the deposit is published and the DOI resolves, cite the GitHub repository/release URL. See [`ZENODO_DOI_PENDING.md`](../ZENODO_DOI_PENDING.md).

## Reproducing the Benchmark

### Quick Smoke Test (< 1 minute, no download needed)

```bash
# Against an in-repo dataset (STORET Rhode Island, full schema):
python benchmark/run_full_benchmark_fixed.py \
  --data data/harmonized/HWIN-STORET-RI/observations.csv \
  --output-dir output/smoke_results \
  --smoke-test

# Or against the canonical GRQA data once downloaded (see Data section):
python benchmark/run_full_benchmark_fixed.py \
  --data <path-to>/HWIN-GRQA-V1-4/observations.csv \
  --output-dir output/benchmark_results \
  --smoke-test
```

Paths can also be set via environment variables `HWIN_DATA_PATH` and
`HWIN_OUTPUT_DIR`.

### Full Canonical Benchmark (certified run: approximately 15.5 hours)

```bash
python benchmark/run_full_benchmark_fixed.py \
  --data <path-to>/HWIN-GRQA-V1-4/observations.csv \
  --output-dir output/benchmark_results/grqa_recomputation
```

Actual execution time depends on hardware, software versions, system load,
and environment; the certified canonical execution recorded ~15.5 hours
(932.4 min) wall-clock on an 8-core CPU (see
`benchmark/reproducibility/CANONICAL_EXECUTION_CERTIFICATE.md`).

**Canonical reference results** (from the certified 15.5 h run):
`benchmark/results/grqa_recomputation/all_results.json` (per-fold values
stored). Since maintenance release 1.0.4 the stored `ci_95` values are
themselves computed from the 5 unique GroupKFold folds (n=5, df=4) —
consistent with `BENCHMARK_STATISTICS.md` and `CI_CORRECTION_REVIEW/`.

### Protocol Compliance

The frozen protocol (`benchmark/protocol/01_HWIN_BENCH_PROTOCOL_v1.0.md`) specifies:

- **Current result artifacts**: GRQA v1.4 results for 11 variables; the frozen protocol document currently specifies a 13-variable scope. This mismatch remains unresolved and must not be represented as full protocol compliance. `MAX_SAMPLES=200,000` and `MIN_SAMPLES=100` are runner eligibility/cap settings.
- **Features**: 7 (lat, lon, year, month, day_of_year, sin_doy, cos_doy)
- **Splits**: 5 unique GroupKFold partitions by station_id. The canonical seed list
  [42, 123, 256, 512, 1024] produces **five deterministic repetitions of the fixed
  partition set** — the seed value is not consumed by any stochastic operation, so
  the 25 recorded evaluations contain 5 unique fold values. Confidence intervals
  are computed on the n=5 unique partitions (df=4) — see `CI_CORRECTION_REVIEW/`.
- **Models**: 7 classical sklearn models with specified hyperparameters
- **Metrics**: MAE, RMSE, R², MAPE, MedAE
- **Statistics**: Corrected 95% CIs (n=5, df=4, t=2.776); statistical testing reserved for v1.1+

**Any deviation is a protocol violation.**

---

## Canonical Results

The certified canonical execution produced results for 11 variables × 7 models across 5 unique GroupKFold partitions × 5 deterministic repetitions (1,925 historical fits). Summary:

| Variable | Best Model | Best R² (mean) | 95% CI (n=5, df=4) | Best RMSE (mean) |
|----------|------------|----------------|---------------------|------------------|
| Water Temperature | Extra Trees | 0.6048 | [0.253, 0.957] | 6.713 |
| pH | Gradient Boosting | 0.0278 | [-0.118, 0.174] | 2.539 |
| Dissolved Oxygen | Ridge | 0.1575 | [-0.003, 0.318] | 13.151 |
| Nitrate Nitrogen | Random Forest | 0.3293 | [0.225, 0.433] | 2.181 |
| Ammonium Nitrogen | Ridge | 0.0011 | [-0.001, 0.003] | 2.092 |
| Phosphate Phosphorus | Linear Regression | 0.0026 | [-0.001, 0.006] | 4.634 |
| DO Percent Saturation | Linear Regression | 0.0008 | [-0.001, 0.002] | 378.648 |
| Total Suspended Solids | Linear Regression | 0.0005 | [-0.001, 0.002] | 3814.820 |
| Total Nitrogen | Gradient Boosting | 0.0216 | [-0.188, 0.231] | 8.618 |
| Total Ammonia Nitrogen | Lasso | 0.0042 | [0.000, 0.008] | 2.981 |
| Nitrite Nitrogen | Random Forest | 0.1703 | [0.036, 0.304] | 0.707 |

**All confidence intervals are CORRECTED** to use n=5 (5 unique GroupKFold partitions), df=4, t=2.776. Original intervals used n=25 (df=24) and were approximately 3× too narrow.

Full results: `benchmark/results/grqa_recomputation/all_results.json`
Per-variable: `benchmark/results/grqa_recomputation/HWIN-VAR-XXX_results.json`
Statistical tests: Reserved for v1.1+ (not executed in v1.0)  
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
  url = {https://github.com/Zakariya-Q/HWIN-Bench}
}
```

Dataset citations (required when using individual datasets):

1. **GRQA v1.4**: Virro, H., Amatulli, G., Kmoch, A., Shen, L., & Uuemaa, E. (2025). *Global River Water Quality Archive (GRQA) (Version 1.4)* [Dataset]. Zenodo. https://doi.org/10.5281/zenodo.15335450

2. **WQP/STORET**: U.S. Geological Survey and Environmental Protection Agency. *Water Quality Portal*. Retrieved 2026-07-08 from https://www.waterqualitydata.us/

See `CITATION.cff` for machine-readable citation metadata.

---

## Dataset Licenses

| Dataset | License | Attribution Required |
|---------|---------|---------------------|
| GRQA v1.4 | CC-BY-4.0 | Yes — see `licenses/ATTRIBUTION.md` |
| WQP/STORET | Source-specific terms; no blanket license assigned | Review contributing agency/source terms and attribute appropriately; see `licenses/DATASET_LICENSE_AUDIT.csv` |

Full license audit: `licenses/DATASET_LICENSE_AUDIT.csv`  
Attribution details: `licenses/ATTRIBUTION.md`

---

## Limitations

1. **GRQA-only regression benchmark**: Only GRQA v1.4 is used for the canonical regression benchmark. STORET/WQP datasets are for transfer learning evaluation (known NaN bug — not certified).

2. **Classical ML only**: v1.0 includes 7 sklearn models. Deep learning (HWIN-Net), XGBoost, LightGBM, CatBoost are reserved for v1.1+.

3. **MAX_SAMPLES cap**: 200,000 observations per variable (10 of 11 variables affected). This is a computational constraint, not a scientific decision.

4. **Spatial/temporal bias**: GRQA overrepresents Europe/North America; tropical/southern hemisphere underrepresented.

5. **No causal claims**: Benchmark measures predictive performance, not causal mechanisms.

6. **Transfer learning NaN bug**: Known issue in transfer evaluation — must be fixed before v1.1.

7. **Statistical testing reserved for v1.1+**: Kruskal-Wallis, Wilcoxon, Cliff's Delta, and Holm-Bonferroni correction are specified in the protocol but NOT implemented in v1.0. Only corrected CIs (n=5, df=4) are provided.

8. **Five seed repetitions are deterministic**: The five seed repetitions produce computationally identical GroupKFold partitions. Only 5 unique fold evaluations exist. CIs correctly use n=5 (df=4).

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
