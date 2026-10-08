# CI CORRECTION DECISION — HWIN-Bench v1.0 (Run B Canonical)

**Date**: 2026-10-08 (v1.0.4 rebuild of the 2026-08-10 correction review)
**Final verdict**: **CI correction only** — all 5 unique fold values are
recoverable from the canonical Run-B artifacts. No model rerun required.

---

## Answers to the required questions

### 1. Were the five seed repetitions actually different?
**NO.** The five seed repetitions (42, 123, 256, 512, 1024) produce
**computationally identical** GroupKFold partitions and model randomness. The
outer seed variable is bound by the loop but never referenced by any
stochastic operation (sampling uses random_state=42; models use
random_state=42; GroupKFold is deterministic given groups). Verified against
the stored Run-B fold values: all 5 repetition blocks are identical for every
one of the 385 metric combinations.

### 2. How many unique fold evaluations exist?
**5 unique fold evaluations** per model-variable-metric. The 25 recorded values
are 5 unique fold values repeated identically 5 times.

### 3. Are n=25 CIs statistically defensible?
**NO.** Treating 25 values as independent underestimates the standard error by
sqrt(5) and uses the wrong degrees of freedom (df=24 instead of df=4).

### 4. What changed and what did not?
- **Unchanged**: point estimates (means), best-model assignments, the 25
  recorded fold values, model definitions, protocol parameters, source data.
- **Changed**: the reported `ci_95` in the canonical JSONs now uses n=5, df=4,
  t=2.7764451051977987; explicit metadata (`n_recorded`, `n_unique_folds`, `ci_n`,
  `ci_df`) documents recorded-vs-unique counts; the benchmark runner computes
  future outputs the same way and fails loudly if the deterministic-repetition
  invariant is broken.

### 5. Was a benchmark rerun required?
**NO.** All corrected statistics are recomputed from the stored fold values.

## Canonical provenance
`benchmark/results/grqa_recomputation/` (Run B). Run A
(`grqa_full_final_groupkfold`) is historical, stored aggregated means only,
and was removed in 1.0.3.

## Numerical evidence
See `CORRECTED_CONFIDENCE_INTERVALS.csv` (385 rows, old n=25 basis vs
corrected n=5 basis) and `CI_CALCULATION_VERIFICATION.md` (two-method
verification, max difference 9.095e-13 <= 1e-12).
