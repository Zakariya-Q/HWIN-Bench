# Changelog

All notable changes to HWIN-Bench v1.0 will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-08-09

### Added
- **Frozen benchmark protocol v1.0** (`benchmark/protocol/01_HWIN_BENCH_PROTOCOL_v1.0.md`) - immutable scientific contract
- **5 canonical datasets** harmonized to Canonical Benchmark Schema (CBS):
  - HWIN-GRQA-V1-4 (Global River Quality Archive v1.4, CC-BY-4.0)
  - HWIN-WQP-SFBAY (USGS/EPA WQP San Francisco Bay, Public Domain)
  - HWIN-STORET-CA (EPA STORET California, Public Domain)
  - HWIN-STORET-TX (EPA STORET Texas, Public Domain)
  - HWIN-STORET-RI (EPA STORET Rhode Island, Public Domain)
- **Canonical Variable Ontology (CVO v1.0)** - 51 variables (HWIN-VAR-001 to HWIN-VAR-051)
- **Variable Synonym Dictionary** - 89 cross-dataset mappings (Tier 1: 52, Tier 2: 28, Tier 3: 9)
- **Unit Harmonization Rules** - 92 conversion rules to SI units
- **Canonical Benchmark Schema (CBS)** - standardized observation/station/variable format
- **7 classical ML models** with fixed hyperparameters (Linear, Ridge, Lasso, ElasticNet, RF, ExtraTrees, GradientBoosting)
- **5×5 GroupKFold cross-validation** by station_id (2,275 total model fits)
- **5 regression metrics**: MAE, RMSE, R², MAPE, MedAE
- **Statistical testing suite**: Kruskal-Wallis, Wilcoxon, Cliff's Delta, Holm-Bonferroni correction
- **95% confidence intervals** via t-distribution
- **Canonical benchmark runner** (`benchmark/run_full_benchmark_fixed.py`) - single entry point
- **Complete provenance chains** for all 5 datasets (raw → harmonized → benchmark)
- **CBS validation engine** (8 completeness, 38 range, 3 referential integrity, 2 duplicate, 4 temporal, 3 spatial rules)
- **Certified canonical execution** - 15.5 hour run independently reproduced
- **Comprehensive documentation** (QUICKSTART, DATA_GUIDE, DATA_DICTIONARY, REPRODUCIBILITY, LIMITATIONS, DATA_PROVENANCE)
- **License audit** for all 5 datasets with evidence (DATASET_LICENSE_AUDIT.csv)
- **Attribution file** for all source datasets (licenses/ATTRIBUTION.md)
- **GitHub-ready release structure** with Git LFS configuration

### Fixed
- **COMP-006**: Fixed GroupKFold split (was using random split instead of station_id grouping)
- **COMP-005**: Integrated transfer learning evaluation code into canonical repository
- **COMP-003**: Parameterized MIN_SAMPLES according to frozen protocol (100 observations)
- **COMP-004**: Fixed NaN handling in transfer learning evaluation

### Protocol Compliance
- All 74 tests pass
- Protocol frozen - any changes require v1.1 with full re-certification
- Canonical execution command: `python benchmark/run_full_benchmark_fixed.py`
- Expected runtime: ~5-6 hours on CPU (n_jobs=-1 for ensemble models)

### Data Integrity
- All 5 datasets pass CBS validation (Gold/Silver certification)
- SHA256 checksums recorded in dataset manifests
- Row counts, columns, variables, units, station IDs verified against canonical inventory
- No canonical benchmark outputs modified

---

## Pre-Release History

### Release Candidate 1 (RC1) - 2026-07-08
- Initial harmonized datasets deposited to `scripts/archive/output_real_hwin_bench_rc1/`
- GRQA v1.4, WQP-SFBAY, STORET-CA/TX/RI canonicalized
- Validation reports generated
- Dataset manifests with checksums created

### Phase 1: Specification Resolution - 2026-06-28 to 2026-07-03
- Frozen protocol specification completed
- Dataset registry established
- Canonical variable ontology (CVO) v1.0 created
- Variable synonym dictionary (89 mappings) created
- Unit harmonization rules (92 rules) created

### Phase 2: Code Resolution - 2026-07-03 to 2026-07-10
- Canonicalization pipeline implemented (mapper, engine, metadata_aligner, unit_converter)
- Baseline models implemented (7 classical sklearn models)
- Evaluation framework (metrics, statistics, confidence intervals)
- CBS validation engine (58 rules)
- Blocker fixes: COMP-003, COMP-004, COMP-005, COMP-006

### Phase 3: Canonical Execution - 2026-07-10 to 2026-07-24
- Canonical benchmark execution (15.5 hours)
- Reproducibility verification
- Statistical testing with Holm-Bonferroni
- Certification documents generated

### Phase 4: Release Compliance Audit - 2026-08-09
- Dataset license audit (5 datasets)
- Derived data classification audit
- GitHub suitability audit
- Public release package prepared