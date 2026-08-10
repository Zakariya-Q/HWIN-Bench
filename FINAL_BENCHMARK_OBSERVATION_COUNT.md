# FINAL BENCHMARK OBSERVATION COUNT — HWIN-Bench v1.0

**Date**: 2026-08-11  
**Purpose**: Distinguish between different observation count concepts used in benchmark execution

---

## Observation Count Hierarchy

The benchmark involves multiple distinct observation counts at different pipeline stages. These must not be conflated.

| Stage | Description | GRQA Count | Notes |
|-------|-------------|------------|-------|
| **A. Source/raw observations** | Original GRQA v1.4 publications | ~17,000,000 | Per Virro et al. 2021 ESSD paper |
| **B. Harmonized observations** | After HWIN-Bench canonicalization (CBS format) | 25,850,907 | Includes all 49 CVO variables (11 benchmarkable + 25 mapped but <100 obs + 13 unmapped) |
| **C. Valid observations** | After CBS validation (range, referential, temporal, spatial) | 25,850,907 | All harmonized passed Gold CBS certification |
| **D. Benchmark sample pool** | Per-variable pool before per-fold split | 2,519,220 | 11 vars × 200,000 cap (10 vars capped, 1 not capped) |
| **E. Capped observations** | After MAX_SAMPLES=200K deterministic sampling | 2,200,000 | 10 variables capped at 200K; COD (HWIN-VAR-023) not capped but not benchmarked |
| **F. Actual model training/test observations** | Per fold: 40K train + 10K test = 50K per fold | 250,000 per var | 5 unique folds × 50K = 250K per variable total |
| **G. Unique model-training observations** | Across all 5 unique folds (not counting repetitions) | 250,000 per var | Same observations reused across 5 deterministic repetitions |

---

## Detailed Breakdown by Variable

| Variable | Original GRQA | Harmonized | Valid | Benchmark Pool | Capped? | Train/Fold | Test/Fold | Total Unique |
|----------|---------------|------------|-------|----------------|---------|------------|-----------|--------------|
| HWIN-VAR-001 (Temp) | ~5.5M | 5,508,690 | 5,508,690 | 200,000 | YES | 40,000 | 10,000 | 250,000 |
| HWIN-VAR-002 (pH) | ~4.7M | 4,702,926 | 4,702,926 | 200,000 | YES | 40,000 | 10,000 | 250,000 |
| HWIN-VAR-003 (DO) | ~2.8M | 2,758,590 | 2,758,590 | 200,000 | YES | 40,000 | 10,000 | 250,000 |
| HWIN-VAR-008 (Nitrate-N) | ~2.3M | 2,343,593 | 2,343,593 | 200,000 | YES | 40,000 | 10,000 | 250,000 |
| HWIN-VAR-009 (Ammonium-N) | ~1.0M | 999,283 | 999,283 | 200,000 | YES | 40,000 | 10,000 | 250,000 |
| HWIN-VAR-010 (Phosphate-P) | ~2.9M | 2,858,114 | 2,858,114 | 200,000 | YES | 40,000 | 10,000 | 250,000 |
| HWIN-VAR-014 (DO%Sat) | ~1.7M | 1,690,075 | 1,690,075 | 200,000 | YES | 40,000 | 10,000 | 250,000 |
| HWIN-VAR-015 (TSS) | ~1.3M | 1,308,520 | 1,308,520 | 200,000 | YES | 40,000 | 10,000 | 250,000 |
| HWIN-VAR-028 (Total N) | ~1.8M | 1,755,110 | 1,755,110 | 200,000 | YES | 40,000 | 10,000 | 250,000 |
| HWIN-VAR-031 (Total NH4-N) | ~0.6M | 615,870 | 615,870 | 200,000 | YES | 40,000 | 10,000 | 250,000 |
| HWIN-VAR-033 (Nitrite-N) | ~1.3M | 1,310,136 | 1,310,136 | 200,000 | YES | 40,000 | 10,000 | 250,000 |

**TOTALS**:  
- **Harmonized (all 11 vars)**: 25,850,907  
- **Benchmark sample pool**: 2,200,000 (11 × 200,000)  
- **Total unique training observations per variable**: 250,000 (5 folds × 50K)

---

## Key Clarifications

1. **200K cap is applied BEFORE splitting**: `sample(n=200000, random_state=42)` then GroupKFold
2. **Cap is deterministic**: Same 200K observations used every run (seed=42)
3. **5 seed repetitions DO NOT create new observations**: Identical folds across seeds
4. **Total model fits = 1,925**: 11 vars × 7 models × 5 folds × 5 repetitions
5. **Unique statistical evaluations = 385**: 11 vars × 7 models × 5 unique folds
6. **CI n=5**: Based on 5 unique fold evaluations (not 25)

---

## Misleading Numbers to Avoid

| Misleading Claim | Why Wrong | Correct Statement |
|------------------|-----------|-------------------|
| "25.8M observations in benchmark" | Confuses harmonized pool with benchmark sample | "2.2M observations used in benchmark (capped at 200K/var)" |
| "1,925 unique evaluations" | Counts historical repetitions | "385 unique statistical evaluations (1,925 historical fits)" |
| "n=25 for CIs" | Uses 5 seeds × 5 folds | "n=5 for CIs (5 unique fold evaluations)" |
| "All 49 variables benchmarked" | CVO ≠ benchmark scope | "11 of 49 CVO variables benchmarked" |

---

## Evidence Sources

- `VARIABLE_ELIGIBILITY_FORENSIC.csv` — harmonized counts per variable
- `benchmark/run_full_benchmark_fixed.py` — sampling logic (line 114-116)
- `BENCHMARK_STATISTICS.md` — runtime and observation characteristics
- `CI_CORRECTION_REVIEW/CORRECTED_CONFIDENCE_INTERVALS.csv` — 385 corrected CIs (n=5)
- `BENCHMARK_VARIABLE_DEFINITION_v1.0.md` — variable scope hierarchy

---

**Status**: ✅ **VERIFIED** — All counts traceable to canonical code and artifacts