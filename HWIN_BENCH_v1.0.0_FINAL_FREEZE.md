# HWIN-Bench v1.0.0 — FINAL FREEZE IDENTITY

**Date**: 2026-08-11  
**Version**: 1.0.0  
**Status**: FROZEN — No further scientific changes permitted

---

## Core Identity

| Property | Value |
|----------|-------|
| **Repository** | https://github.com/Zakariya-Q/HWIN-Bench |
| **Release Tag** | v1.0.0 |
| **Commit (v1.0.0)** | 1b22d1447975271e93e2f77c673ab00b54e0919a |
| **Commit (v1.0-final-freeze)** | [this commit] |
| **Protocol** | Frozen v1.0 (`benchmark/protocol/01_HWIN_BENCH_PROTOCOL_v1.0.md`) |
| **DOI (reserved)** | 10.5281/zenodo.21877825 |

---

## Canonical Benchmark Scope (FROZEN)

### Benchmark Variables (11 — EXACTLY THESE)
1. **HWIN-VAR-001** — Water Temperature
2. **HWIN-VAR-002** — pH
3. **HWIN-VAR-003** — Dissolved Oxygen
4. **HWIN-VAR-008** — Nitrate Nitrogen
5. **HWIN-VAR-009** — Ammonium Nitrogen
6. **HWIN-VAR-010** — Phosphate Phosphorus
7. **HWIN-VAR-014** — Dissolved Oxygen Percent Saturation
8. **HWIN-VAR-015** — Total Suspended Solids
9. **HWIN-VAR-028** — Total Nitrogen
10. **HWIN-VAR-031** — Total Ammonia Nitrogen
11. **HWIN-VAR-033** — Nitrite Nitrogen

### CVO Variables (49 — FULL ONTOLOGY)
**HWIN-VAR-001 through HWIN-VAR-049** (see `ontology/canonical_variable_ontology.csv`)

### Models (7 — FROZEN)
1. Linear Regression
2. Ridge (alpha=1.0)
3. Lasso (alpha=0.1)
4. ElasticNet (alpha=0.1, l1_ratio=0.5)
5. Random Forest (200 trees, random_state=42)
6. Extra Trees (200 trees, random_state=42)
7. Gradient Boosting (200 trees, learning_rate=0.1, max_depth=3, random_state=42)

### Cross-Validation (FROZEN)
- **Split Method**: GroupKFold by `station_id`
- **Unique Partitions**: 5
- **Seed Repetitions**: 5 deterministic ([42, 123, 256, 512, 1024])
- **Unique Fold Evaluations per Model-Variable**: 5
- **Total Historical Fit Invocations**: 1,925 (11 × 7 × 5 × 5)
- **Total Unique Statistical Evaluations**: 385 (11 × 7 × 5)

### Statistical Parameters (FROZEN)
- **CI Sample Size (n)**: 5
- **CI Degrees of Freedom (df)**: 4
- **CI t-critical (95%)**: 2.776
- **CI Correction**: Applied (n=25 → n=5, width ratio = 3.008)

### Data Parameters (FROZEN)
- **Primary Dataset**: GRQA v1.4 (Zenodo 10.5281/zenodo.15335450)
- **MAX_SAMPLES**: 200,000 per variable (deterministic, seed=42)
- **MIN_SAMPLES**: 100 (eligibility threshold)
- **Features**: 7 (lat, lon, year, month, day_of_year, sin_doy, cos_doy)
- **Metrics**: MAE, RMSE, R², MAPE, MedAE

### Runtime (FROZEN)
- **Wall-clock time**: 15.5 hours (932.4 minutes)
- **Model time sum**: 528.4 minutes (31,703.9 seconds)
- **Variable time sum**: 593.8 minutes

---

## What Is NOT in v1.0 (Explicit Exclusions)

The following are **explicitly excluded** from the v1.0 canonical regression benchmark:

| Excluded | Reason |
|----------|--------|
| **BOD (HWIN-VAR-022)** | Mapping exists but 0 harmonized observations |
| **COD (HWIN-VAR-023)** | Mapping exists but 0 harmonized observations |
| **Turbidity (HWIN-VAR-004)** | No GRQA mapping in synonym dictionary |
| **Specific Conductance (HWIN-VAR-005)** | No GRQA mapping in synonym dictionary |
| **Flow Rate (HWIN-VAR-006)** | No GRQA mapping |
| **Water Depth (HWIN-VAR-007)** | No GRQA mapping |
| **Chlorophyll-a (HWIN-VAR-011)** | No GRQA mapping |
| **Fecal Coliforms (HWIN-VAR-012)** | No GRQA mapping |
| **Water Temp at Depth (HWIN-VAR-013)** | No GRQA mapping |
| **Air Temperature (HWIN-VAR-016)** | No GRQA mapping |
| **Chloride (HWIN-VAR-017)** | No GRQA mapping |
| **Sulfate (HWIN-VAR-018)** | No GRQA mapping |
| **Silica (HWIN-VAR-019)** | No GRQA mapping |
| **Alkalinity (HWIN-VAR-020)** | No GRQA mapping |
| **Total Dissolved Solids (HWIN-VAR-021)** | No GRQA mapping |
| **DIN/TDN/TIN/TKN/DON/TON/DKN (HWIN-VAR-024 to 032)** | Mappings exist but 0 harmonized observations |
| **DIP/TDP/TIP/TOP/POP/TPP (HWIN-VAR-034 to 039)** | Mappings exist but 0 harmonized observations |
| **TC/DIC/DOC/TIC/TOC/PC/PIC/POC/PN/PON (HWIN-VAR-040 to 049)** | Mappings exist but 0 harmonized observations |
| **Statistical Testing (Kruskal-Wallis, Wilcoxon, Cliff's Delta, Holm-Bonferroni)** | Specified in protocol but NOT implemented in v1.0 |
| **Deep Learning Models (HWIN-Net)** | Reserved for v1.1+ |
| **XGBoost, LightGBM, CatBoost** | Reserved for v1.1+ |
| **Spatial/Temporal CV** | Reserved for v1.1+ |
| **Transfer Learning (certified)** | Known NaN bug; not certified |

---

## What Is PRESERVED in v1.0 (Historical Evidence)

The following are **preserved as historical/exclusion evidence**:

- `VARIABLE_ELIGIBILITY_FORENSIC.csv` — Full 49-variable eligibility audit
- `BENCHMARK_VARIABLE_DEFINITION_v1.0.md` — Variable scope hierarchy
- `PROTOCOL_RECONCILIATION_v1.0_TO_v1.1.md` — Protocol vs execution reconciliation
- `BENCHMARK_STATISTICS.md` — Benchmark summary with corrected CIs
- `CI_CORRECTION_REVIEW/` — Complete CI correction evidence (385 CIs)
- `docs/LIMITATIONS.md` — Explicit documentation of all v1.0 limitations
- `docs/DATA_PROVENANCE.md` — Full provenance chains
- `CANONICAL_EXECUTION_CERTIFICATE.md` — Reproducibility certificate
- `FINAL_V1.0_DATASET_COUNTS.md/csv` — Authoritative dataset counts
- `FINAL_BENCHMARK_OBSERVATION_COUNT.md` — Observation accounting hierarchy

---

## Files in v1.0 Release (Canonical)

### Core Benchmark
- `benchmark/protocol/01_HWIN_BENCH_PROTOCOL_v1.0.md` — Frozen protocol (IMMUTABLE)
- `benchmark/run_full_benchmark_fixed.py` — Canonical benchmark runner
- `benchmark/results/GRQA_full_benchmark_complete_CORRECTED.json` — Master results
- `benchmark/results/HWIN-VAR-XXX_results.json` — Per-variable results

### Documentation
- `README.md` — Final public release README
- `CITATION.cff` — Citation metadata (DOI: 10.5281/zenodo.21877825)
- `LICENSE` — CC-BY-4.0 + dataset licenses
- `docs/LIMITATIONS.md` — v1.0 limitations
- `docs/DATA_GUIDE.md` — Data access guide
- `docs/DATA_DICTIONARY.md` — Schema and variable definitions
- `docs/REPRODUCIBILITY.md` — Reproduction instructions
- `docs/DATA_PROVENANCE.md` — Provenance chains
- `docs/QUICKSTART.md` — Quickstart guide

### Data (GitHub)
- `data/harmonized/HWIN-GRQA-V1-4/` — stations.json, variables.csv, dataset.json
- `data/harmonized/HWIN-WQP-SFBAY/` — All CBS files
- `data/harmonized/HWIN-STORET-CA/` — All CBS files
- `data/harmonized/HWIN-STORET-TX/` — All CBS files
- `data/harmonized/HWIN-STORET-RI/` — All CBS files
- `data/manifests/DATASET_RELEASE_INVENTORY.csv` — Dataset inventory
- `data/manifests/DERIVED_DATA_AUDIT.csv` — Derived data audit

### Ontology
- `ontology/canonical_variable_ontology.csv` — 49 variables
- `ontology/variable_synonym_dictionary.csv` — 89 mappings
- `ontology/unit_harmonization_rules.csv` — 92 rules

### Figures & Tables
- `paper/figures/fig5_benchmark_CORRECTED.png/pdf/svg` — Corrected benchmark figure
- `paper/figures/fig7_missing_data_robustness.png/pdf/svg` — Robustness figure
- `paper/tables/Table5_grqa_CORRECTED.tex` — Corrected benchmark table (11 vars)

### Audit & Evidence
- `CI_CORRECTION_REVIEW/CORRECTED_CONFIDENCE_INTERVALS.csv` — 385 corrected CIs
- `CI_CORRECTION_REVIEW/CI_CORRECTION_DECISION.md` — Correction decision
- `FINAL_V1.0_DATASET_COUNTS.md/csv` — Dataset counts
- `FINAL_BENCHMARK_OBSERVATION_COUNT.md` — Observation accounting
- `HWIN_BENCH_v1.0.0_FINAL_FREEZE.md` — This document

---

## Scientific Integrity Guarantees

| Guarantee | Verification |
|-----------|--------------|
| ✅ No benchmark retraining | Frozen protocol + frozen code |
| ✅ No point estimate changes | `CI_CORRECTION_REVIEW/CORRECTED_CONFIDENCE_INTERVALS.csv` shows `old_mean == corrected_mean` |
| ✅ No CI changes | All 385 corrected CIs verified (width ratio = 3.008) |
| ✅ No dataset changes | Dataset manifests + checksums preserved |
| ✅ No protocol changes | `01_HWIN_BENCH_PROTOCOL_v1.0.md` is immutable |
| ✅ No variable scope expansion | 11 variables frozen; 49 CVO preserved as ontology |

---

## Future Expansion (v1.1+)

All future work targets v1.1+:

| Feature | Repository |
|---------|------------|
| XGBoost, LightGBM, CatBoost | `hwin-baselines` |
| HWIN-Net Deep Learning | `hwin-net` |
| Spatial Block CV | Design phase |
| Temporal CV | Design phase |
| Statistical Testing | v1.1+ protocol |
| Prediction Intervals | Research needed |
| Watershed Features | Data acquisition |
| Global Transfer Benchmark | More target regions |

---

## Final Certification

**HWIN-Bench v1.0.0 FINAL FREEZE — APPROVED (Grade A)**

- All 11 benchmark variables verified against canonical results
- All 385 corrected CIs verified (n=5, df=4, t=2.776)
- Point estimates unchanged (bitwise identical)
- 49-variable CVO preserved as ontology (not benchmark scope)
- All excluded variables documented with evidence
- No stale claims remain in public-facing documentation
- DOI reserved: 10.5281/zenodo.21877825
- Repository: https://github.com/Zakariya-Q/HWIN-Bench

**This freeze is immutable. No scientific changes to v1.0.0 are permitted.**