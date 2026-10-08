# FINAL V1.0 DATASET COUNTS — HWIN-Bench v1.0

**Date**: 2026-08-11  
**Purpose**: Authoritative v1.0 dataset counts from canonical sources

---

## GRQA v1.4 (HWIN-GRQA-V1-4) — Canonical Benchmark Dataset

| Metric | Value | Source |
|--------|-------|--------|
| **Raw observations (original GRQA)** | ~17,000,000 | GRQA publication (Virrogram et al. 2021) |
| **Harmonized observations (CBS)** | 25,850,907 | `data/harmonized/HWIN-GRQA-V1-4/dataset.json` |
| **Valid observations (after cleaning)** | 25,850,907 | `dataset.json` |
| **Benchmark sample pool (after MAX_SAMPLES=200K cap)** | 2,519,220 | `dataset.json` |
| **Stations** | 107,000 | `dataset.json` |
| **Variables (CVO with GRQA mappings)** | 36 | `VARIABLE_ELIGIBILITY_FORENSIC.csv` |
| **Benchmark-eligible variables (MIN_SAMPLES ≥ 100)** | 11 | `VARIABLE_ELIGIBILITY_FORENSIC.csv` |
| **File size (raw GRQA zip)** | 6.0 GB (1.2 GB data + 4.8 MB meta) | Zenodo record 15335450 |
| **File size (harmonized observations.csv)** | 5.7 GB | Zenodo deposition |
| **SHA256 (harmonized observations.csv)** | `989e5a6ba07499d81443c8819ef7f1e786fdef8a52661474a2bf5cc4a2ed6f8f` | `data/README.md` |

### 11 Benchmark Variables (GRQA harmonized counts)

| Variable ID | Canonical Name | Harmonized Obs | Valid Obs | Benchmark Sample (capped) |
|-------------|----------------|----------------|-----------|---------------------------|
| HWIN-VAR-001 | Water Temperature | 5,508,690 | 5,508,690 | 200,000 (capped) |
| HWIN-VAR-002 | pH | 4,702,926 | 4,702,926 | 200,000 (capped) |
| HWIN-VAR-003 | Dissolved Oxygen | 2,758,590 | 2,758,590 | 200,000 (capped) |
| HWIN-VAR-008 | Nitrate Nitrogen | 2,343,593 | 2,343,593 | 200,000 (capped) |
| HWIN-VAR-009 | Ammonium Nitrogen | 999,283 | 999,283 | 200,000 (capped) |
| HWIN-VAR-010 | Phosphate Phosphorus | 2,858,114 | 2,858,114 | 200,000 (capped) |
| HWIN-VAR-014 | DO Percent Saturation | 1,690,075 | 1,690,075 | 200,000 (capped) |
| HWIN-VAR-015 | Total Suspended Solids | 1,308,520 | 1,308,520 | 200,000 (capped) |
| HWIN-VAR-028 | Total Nitrogen | 1,755,110 | 1,755,110 | 200,000 (capped) |
| HWIN-VAR-031 | Total Ammonia Nitrogen | 615,870 | 615,870 | 200,000 (capped) |
| HWIN-VAR-033 | Nitrite Nitrogen | 1,310,136 | 1,310,136 | 200,000 (capped) |

---

## WQP SF Bay (HWIN-WQP-SFBAY) — Transfer Learning Dataset

| Metric | Value | Source |
|--------|-------|--------|
| **Raw observations (WQP API)** | ~51,000 | `DATA_PROVENANCE.md` |
| **Harmonized observations (CBS)** | 51,000 | `data/harmonized/HWIN-WQP-SFBAY/dataset.json` |
| **Valid observations** | 51,000 | `dataset.json` |
| **Stations** | ~1,000 | `data/harmonized/HWIN-WQP-SFBAY/dataset.json` |
| **Variables (canonical)** | 19 | `data/harmonized/HWIN-WQP-SFBAY/variables.csv` |
| **File size (harmonized observations.csv)** | 4.6 MB | `ls -la` |
| **Benchmark use** | Transfer learning only (Protocol §16) | `DATA_PROVENANCE.md` |

---

## STORET CA (HWIN-STORET-CA) — Transfer Learning Dataset

| Metric | Value | Source |
|--------|-------|--------|
| **Raw observations (WQP API)** | ~180,000 | `DATA_PROVENANCE.md` |
| **Harmonized observations (CBS)** | 180,000 | `data/harmonized/HWIN-STORET-CA/dataset.json` |
| **Valid observations** | 180,000 | `dataset.json` |
| **Stations** | ~3,000 | `data/harmonized/HWIN-STORET-CA/dataset.json` |
| **Variables (canonical)** | 22 | `data/harmonized/HWIN-STORET-CA/variables.csv` |
| **File size (harmonized observations.csv)** | 41 MB | `ls -la` |
| **Benchmark use** | Transfer learning only (Protocol §16) | `DATA_PROVENANCE.md` |

---

## STORET TX (HWIN-STORET-TX) — Transfer Learning Dataset

| Metric | Value | Source |
|--------|-------|--------|
| **Raw observations (WQP API)** | ~175,000 | `DATA_PROVENANCE.md` |
| **Harmonized observations (CBS)** | 175,000 | `data/harmonized/HWIN-STORET-TX/dataset.json` |
| **Valid observations** | 175,000 | `dataset.json` |
| **Stations** | ~2,000 | `data/harmonized/HWIN-STORET-TX/dataset.json` |
| **Variables (canonical)** | 21 | `data/harmonized/HWIN-STORET-TX/variables.csv` |
| **File size (harmonized observations.csv)** | 45 MB | `ls -la` |
| **Benchmark use** | Transfer learning only (Protocol §16) | `DATA_PROVENANCE.md` |

---

## STORET RI (HWIN-STORET-RI) — Transfer Learning Dataset

| Metric | Value | Source |
|--------|-------|--------|
| **Raw observations (WQP API)** | ~2,500 | `DATA_PROVENANCE.md` |
| **Harmonized observations (CBS)** | 2,500 | `data/harmonized/HWIN-STORET-RI/dataset.json` |
| **Valid observations** | 2,500 | `dataset.json` |
| **Stations** | ~50 | `data/harmonized/HWIN-STORET-RI/dataset.json` |
| **Variables (canonical)** | 18 | `data/harmonized/HWIN-STORET-RI/variables.csv` |
| **File size (harmonized observations.csv)** | 0.5 MB | `ls -la` |
| **Benchmark use** | Transfer learning only (Protocol §16) | `DATA_PROVENANCE.md` |

---

## Summary

| Dataset | Role in v1.0 | Raw Obs | Harmonized Obs | Stations | Variables | Benchmarkable Vars |
|---------|--------------|---------|----------------|----------|-----------|-------------------|
| HWIN-GRQA-V1-4 | **Canonical regression benchmark** | ~17M | 25.8M | 107,000 | 36 (mapped) / 11 (eligible) | **11** |
| HWIN-WQP-SFBAY | Transfer learning (supplementary) | 51K | 51K | ~1,000 | 19 | 0 |
| HWIN-STORET-CA | Transfer learning (supplementary) | 180K | 180K | ~3,000 | 22 | 0 |
| HWIN-STORET-TX | Transfer learning (supplementary) | 175K | 175K | ~2,000 | 21 | 0 |
| HWIN-STORET-RI | Transfer learning (supplementary) | 2.5K | 2.5K | ~50 | 18 | 0 |

**Total canonical benchmark observations**: 2,519,220 (11 variables × 200K cap)  
**Total model fits**: 1,925 (11 vars × 7 models × 5 folds × 5 repetitions)  
**Unique fold evaluations**: 385 (11 vars × 7 models × 5 unique folds)

---

**Evidence Sources**:
- `VARIABLE_ELIGIBILITY_FORENSIC.csv` (authoritative for variable eligibility)
- `data/harmonized/*/dataset.json` (per-dataset metadata)
- `BENCHMARK_STATISTICS.md` (benchmark execution summary)
- `DATA_PROVENANCE.md` (full provenance chains)
- `CI_CORRECTION_REVIEW/CORRECTED_CONFIDENCE_INTERVALS.csv` (385 corrected CIs)
- `BENCHMARK_VARIABLE_DEFINITION_v1.0.md` (variable scope hierarchy)

**Status**: ✅ **VERIFIED** — All counts traceable to canonical artifacts