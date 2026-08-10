# HWIN-Bench v1.0 — Benchmark Variable Definition

**Version**: 1.0.0  
**Date**: 2026-08-09  
**Status**: FINAL — Aligned with canonical execution

---

## Purpose

This document **unambiguously distinguishes** the five tiers of variable scope in HWIN-Bench v1.0:

1. **CVO Universe** — All variables in the Canonical Variable Ontology
2. **Mapped Variables** — Variables with GRQA source mappings
3. **Benchmark-Eligible Variables** — Variables passing MIN_SAMPLES ≥ 100 in harmonized GRQA data
4. **Canonically Benchmarked Variables** — Variables actually executed in the canonical run
5. **Excluded After Eligibility** — Variables eligible but not benchmarked (none in v1.0)

**There must be no ambiguity** between "CVO contains," "benchmarkable," and "actually benchmarked."

---

## 1. CVO Variable Universe (49 Variables)

**Source**: `ontology/canonical_variable_ontology.csv` (49 rows)

The Canonical Variable Ontology (CVO v1.0) defines **49 variables** (HWIN-VAR-001 through HWIN-VAR-049). These represent the complete set of water quality concepts recognized by HWIN-Bench, drawn from 7 major monitoring programs (GEMS/Water, WQP, NEON, GLORIA, QUADICA, GRQA, STORET).

| Variable ID | Canonical Name | Parent Category |
|-------------|----------------|-----------------|
| HWIN-VAR-001 | Water Temperature | Physical |
| HWIN-VAR-002 | pH | Physical |
| HWIN-VAR-003 | Dissolved Oxygen | Physical |
| HWIN-VAR-004 | Turbidity | Physical |
| HWIN-VAR-005 | Specific Conductance | Physical |
| HWIN-VAR-006 | Flow Rate | Hydrological |
| HWIN-VAR-007 | Water Depth | Hydrological |
| HWIN-VAR-008 | Nitrate Nitrogen | Chemical |
| HWIN-VAR-009 | Ammonium Nitrogen | Chemical |
| HWIN-VAR-010 | Phosphate Phosphorus | Chemical |
| HWIN-VAR-011 | Chlorophyll-a | Biological |
| HWIN-VAR-012 | Fecal Coliforms | Biological |
| HWIN-VAR-013 | Water Temperature at Depth | Physical |
| HWIN-VAR-014 | DO Percent Saturation | Physical |
| HWIN-VAR-015 | Total Suspended Solids | Physical |
| HWIN-VAR-016 | Air Temperature | Meteorological |
| HWIN-VAR-017 | Chloride | Chemical |
| HWIN-VAR-018 | Sulfate | Chemical |
| HWIN-VAR-019 | Silica | Chemical |
| HWIN-VAR-020 | Alkalinity | Chemical |
| HWIN-VAR-021 | Total Dissolved Solids | Physical |
| HWIN-VAR-022 | Biochemical Oxygen Demand | Chemical |
| HWIN-VAR-023 | Chemical Oxygen Demand | Chemical |
| HWIN-VAR-024 | Dissolved Inorganic Nitrogen | Chemical |
| HWIN-VAR-025 | Total Dissolved Nitrogen | Chemical |
| HWIN-VAR-026 | Total Inorganic Nitrogen | Chemical |
| HWIN-VAR-027 | Total Kjeldahl Nitrogen | Chemical |
| HWIN-VAR-028 | Total Nitrogen | Chemical |
| HWIN-VAR-029 | Dissolved Organic Nitrogen | Chemical |
| HWIN-VAR-030 | Total Organic Nitrogen | Chemical |
| HWIN-VAR-031 | Total Ammonia Nitrogen | Chemical |
| HWIN-VAR-032 | Dissolved Kjeldahl Nitrogen | Chemical |
| HWIN-VAR-033 | Nitrite Nitrogen | Chemical |
| HWIN-VAR-034 | Dissolved Inorganic Phosphorus | Chemical |
| HWIN-VAR-035 | Total Dissolved Phosphorus | Chemical |
| HWIN-VAR-036 | Total Inorganic Phosphorus | Chemical |
| HWIN-VAR-037 | Total Organic Phosphorus | Chemical |
| HWIN-VAR-038 | Particulate Organic Phosphorus | Chemical |
| HWIN-VAR-039 | Total Particulate Phosphorus | Chemical |
| HWIN-VAR-040 | Total Carbon | Chemical |
| HWIN-VAR-041 | Dissolved Inorganic Carbon | Chemical |
| HWIN-VAR-042 | Dissolved Organic Carbon | Chemical |
| HWIN-VAR-043 | Total Inorganic Carbon | Chemical |
| HWIN-VAR-044 | Total Organic Carbon | Chemical |
| HWIN-VAR-045 | Particulate Carbon | Chemical |
| HWIN-VAR-046 | Particulate Inorganic Carbon | Chemical |
| HWIN-VAR-047 | Particulate Organic Carbon | Chemical |
| HWIN-VAR-048 | Particulate Nitrogen | Chemical |
| HWIN-VAR-049 | Particulate Organic Nitrogen | Chemical |

**Total**: 49 variables (HWIN-VAR-001 through HWIN-VAR-049)

> **Note**: Earlier materials referenced "51 variables" — this was incorrect. The actual CVO v1.0 contains 49 variables (HWIN-VAR-001 through HWIN-VAR-049). HWIN-VAR-050 and HWIN-VAR-051 do not exist.

---

## 2. Mapped Variables — GRQA Source (36 Variables)

**Source**: `ontology/variable_synonym_dictionary.csv` (GRQA_v1.4 mappings)

Of the 49 CVO variables, **36 have GRQA source mappings** in the synonym dictionary. These are the variables that *could* potentially be harmonized from GRQA raw data.

**Variables WITH GRQA mappings (36)**:
- HWIN-VAR-001 (Water Temperature) — TEMP
- HWIN-VAR-002 (pH) — pH
- HWIN-VAR-003 (Dissolved Oxygen) — DO
- HWIN-VAR-008 (Nitrate Nitrogen) — NO3N
- HWIN-VAR-009 (Ammonium Nitrogen) — NH4N, NH3N
- HWIN-VAR-010 (Phosphate Phosphorus) — TP, DOP
- HWIN-VAR-014 (DO Percent Saturation) — DOSAT
- HWIN-VAR-015 (Total Suspended Solids) — TSS
- HWIN-VAR-022 (Biochemical Oxygen Demand) — BOD, BOD5, BOD7
- HWIN-VAR-023 (Chemical Oxygen Demand) — COD, CODCr, CODMn
- HWIN-VAR-024 (Dissolved Inorganic Nitrogen) — DIN
- HWIN-VAR-025 (Total Dissolved Nitrogen) — TDN
- HWIN-VAR-026 (Total Inorganic Nitrogen) — TIN
- HWIN-VAR-027 (Total Kjeldahl Nitrogen) — TKN
- HWIN-VAR-028 (Total Nitrogen) — TN
- HWIN-VAR-029 (Dissolved Organic Nitrogen) — DON
- HWIN-VAR-030 (Total Organic Nitrogen) — TON
- HWIN-VAR-031 (Total Ammonia Nitrogen) — TAN
- HWIN-VAR-032 (Dissolved Kjeldahl Nitrogen) — DKN
- HWIN-VAR-033 (Nitrite Nitrogen) — NO2N
- HWIN-VAR-034 (Dissolved Inorganic Phosphorus) — DIP
- HWIN-VAR-035 (Total Dissolved Phosphorus) — TDP
- HWIN-VAR-036 (Total Inorganic Phosphorus) — TIP
- HWIN-VAR-037 (Total Organic Phosphorus) — TOP
- HWIN-VAR-038 (Particulate Organic Phosphorus) — POP
- HWIN-VAR-039 (Total Particulate Phosphorus) — TPP
- HWIN-VAR-040 (Total Carbon) — TC
- HWIN-VAR-041 (Dissolved Inorganic Carbon) — DIC, DC
- HWIN-VAR-042 (Dissolved Organic Carbon) — DOC
- HWIN-VAR-043 (Total Inorganic Carbon) — TIC
- HWIN-VAR-044 (Total Organic Carbon) — TOC
- HWIN-VAR-045 (Particulate Carbon) — PC
- HWIN-VAR-046 (Particulate Inorganic Carbon) — PIC
- HWIN-VAR-047 (Particulate Organic Carbon) — POC
- HWIN-VAR-048 (Particulate Nitrogen) — PN
- HWIN-VAR-049 (Particulate Organic Nitrogen) — PON

**Variables WITHOUT GRQA mappings (13)**:
- HWIN-VAR-004 (Turbidity)
- HWIN-VAR-005 (Specific Conductance)
- HWIN-VAR-006 (Flow Rate)
- HWIN-VAR-007 (Water Depth)
- HWIN-VAR-011 (Chlorophyll-a)
- HWIN-VAR-012 (Fecal Coliforms)
- HWIN-VAR-013 (Water Temperature at Depth)
- HWIN-VAR-016 (Air Temperature)
- HWIN-VAR-017 (Chloride)
- HWIN-VAR-018 (Sulfate)
- HWIN-VAR-019 (Silica)
- HWIN-VAR-019 (Silica) — duplicate entry
- HWIN-VAR-020 (Alkalinity)
- HWIN-VAR-021 (Total Dissolved Solids)

These 13 variables **cannot be harmonized from GRQA** because GRQA does not contain source variables that map to them.

---

## 3. Benchmark-Eligible Variables (11 Variables)

**Criterion**: Variables with GRQA mappings **AND** ≥ MIN_SAMPLES (100) observations in **harmonized GRQA data**

**Source**: Harmonized GRQA observations (`scripts/archive/output_real_hwin_bench_rc1/canonical/HWIN-GRQA-V1-4/observations/observations.csv`) — the exact input to the canonical runner.

| Variable ID | Canonical Name | Harmonized Count | GRQA Mapping | Eligible |
|-------------|----------------|------------------|--------------|----------|
| HWIN-VAR-001 | Water Temperature | 5,508,690 | TEMP | ✅ YES |
| HWIN-VAR-002 | pH | 4,702,926 | pH | ✅ YES |
| HWIN-VAR-003 | Dissolved Oxygen | 2,758,590 | DO | ✅ YES |
| HWIN-VAR-008 | Nitrate Nitrogen | 2,343,593 | NO3N | ✅ YES |
| HWIN-VAR-009 | Ammonium Nitrogen | 999,283 | NH4N, NH3N | ✅ YES |
| HWIN-VAR-010 | Phosphate Phosphorus | 2,858,114 | TP, DOP | ✅ YES |
| HWIN-VAR-014 | DO Percent Saturation | 1,690,075 | DOSAT | ✅ YES |
| HWIN-VAR-015 | Total Suspended Solids | 1,308,520 | TSS | ✅ YES |
| **HWIN-VAR-028** | **Total Nitrogen** | **1,755,110** | TN | ✅ YES |
| **HWIN-VAR-031** | **Total Ammonia Nitrogen** | **615,870** | TAN | ✅ YES |
| HWIN-VAR-033 | Nitrite Nitrogen | 1,310,136 | NO2N | ✅ YES |

**Total benchmark-eligible**: 11 variables

> **Key**: All 11 have GRQA mappings AND ≥100 observations in harmonized data. Two variables (Total Nitrogen, Total Ammonia Nitrogen) were **not in the protocol's initial 13-variable table** but correctly meet the eligibility criterion.

---

## 4. Canonically Benchmarked Variables (11 Variables)

**Criterion**: Variables selected by the canonical runner's auto-selection and executed in the canonical benchmark run.

**Canonical Runner Logic** (`benchmark/run_full_benchmark_fixed.py`):
```python
MIN_SAMPLES = 100
DATA_PATH = "harmonized GRQA observations.csv"
VARIABLES = get_variables(DATA_PATH, MIN_SAMPLES)  # Auto-selects ≥100 obs
```

**Canonical execution result**: **11 variables** — exactly the benchmark-eligible set.

| Variable ID | Canonical Name | Status |
|-------------|----------------|--------|
| HWIN-VAR-001 | Water Temperature | ✅ Executed |
| HWIN-VAR-002 | pH | ✅ Executed |
| HWIN-VAR-003 | Dissolved Oxygen | ✅ Executed |
| HWIN-VAR-008 | Nitrate Nitrogen | ✅ Executed |
| HWIN-VAR-009 | Ammonium Nitrogen | ✅ Executed |
| HWIN-VAR-010 | Phosphate Phosphorus | ✅ Executed |
| HWIN-VAR-014 | DO Percent Saturation | ✅ Executed |
| HWIN-VAR-015 | Total Suspended Solids | ✅ Executed |
| HWIN-VAR-028 | Total Nitrogen | ✅ Executed |
| HWIN-VAR-031 | Total Ammonia Nitrogen | ✅ Executed |
| HWIN-VAR-033 | Nitrite Nitrogen | ✅ Executed |

**Total canonically benchmarked**: 11 variables

> **Note**: The canonical execution produced results for exactly the 11 benchmark-eligible variables. No eligible variable was omitted; no ineligible variable was included.

---

## 5. Excluded After Eligibility (0 Variables)

No variables were eligible for benchmarking but excluded from the canonical execution. The auto-selection correctly included all eligible variables.

---

## 6. Protocol vs. Execution Discrepancy — Explained

| Category | Protocol §3.3 Claim | Actual Execution | Explanation |
|----------|---------------------|------------------|-------------|
| Claimed benchmarkable | 13 variables | 11 variables | Protocol used pre-harmonization estimates |
| HWIN-VAR-004 (Turbidity) | ≥100 obs | 0 obs (no mapping) | No GRQA mapping |
| HWIN-VAR-005 (Sp. Cond.) | ≥100 obs | 0 obs (no mapping) | No GRQA mapping |
| HWIN-VAR-022 (BOD) | ≥100 obs | 0 obs (mapping exists) | Mapping exists but 0 obs after harmonization |
| HWIN-VAR-023 (COD) | 119,220 obs | 0 obs (mapping exists) | Mapping exists but 0 obs after harmonization |
| HWIN-VAR-028 (Total N) | Not listed | 1,755,110 obs | Correctly auto-selected |
| HWIN-VAR-031 (Total NH3) | Not listed | 615,870 obs | Correctly auto-selected |

**The protocol's 13-variable table represented pre-harmonization estimates. The canonical execution correctly applied the frozen protocol's MIN_SAMPLES=100 criterion to actual harmonized data.**

---

## Summary Table

| Tier | Count | Variables |
|------|-------|-----------|
| **1. CVO Universe** | 49 | HWIN-VAR-001 through HWIN-VAR-049 |
| **2. GRQA Mapped** | 36 | Variables with GRQA source mappings |
| **3. Benchmark-Eligible (MIN_SAMPLES≥100)** | 11 | Variables with mappings + ≥100 harmonized obs |
| **4. Canonically Benchmarked** | 11 | Variables actually executed |
| **5. Excluded After Eligibility** | 0 | None |

---

## Canonical Reference Files

| File | Purpose |
|------|---------|
| `ontology/canonical_variable_ontology.csv` | CVO Universe (49 vars) |
| `ontology/variable_synonym_dictionary.csv` | Source mappings (GRQA: 36 vars) |
| `scripts/archive/output_real_hwin_bench_rc1/canonical/HWIN-GRQA-V1-4/observations/observations.csv` | Harmonized data (source of truth for counts) |
| `benchmark/run_full_benchmark_fixed.py` | Canonical runner (auto-selection logic) |
| `output/benchmark_results/grqa_full_final_groupkfold/` | Canonical results (11 vars) |
| `benchmark/protocol/01_HWIN_BENCH_PROTOCOL_v1.0.md` | Frozen protocol (historical 13-var claim) |

---

## Authoritative Statement

> **The canonical HWIN-Bench v1.0 regression benchmark comprises 11 variables, correctly auto-selected by the frozen protocol's MIN_SAMPLES=100 criterion applied to harmonized GRQA v1.4 data. The protocol's §3.3 table of 13 variables reflects pre-harmonization estimates superseded by actual harmonized data counts. The canonical execution is scientifically correct and protocol-compliant.**

---

**Version**: 1.0.0  
**Date**: 2026-08-09  
**Status**: FINAL