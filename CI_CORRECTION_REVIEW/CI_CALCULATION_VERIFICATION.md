# CI Calculation Verification

**Date**: 2026-08-09  
**Purpose**: Independent verification of CI calculation using two methods

---

## Methods Tested

### Method A: Direct Formula Implementation
```python
def ci_direct(vals, confidence=0.95):
    vals = np.array([v for v in vals if not np.isnan(v)])
    n = len(vals)
    if n < 2:
        return [np.nan, np.nan]
    m = np.mean(vals)
    se = stats.sem(vals)
    h = se * stats.t.ppf((1 + confidence) / 2., n - 1)
    return [float(m - h), float(m + h)]
```

### Method B: SciPy's `stats.t.interval`
```python
def ci_scipy(vals, confidence=0.95):
    vals = np.array([v for v in vals if not np.isnan(v)])
    n = len(vals)
    if n < 2:
        return [np.nan, np.nan]
    return list(stats.t.interval(confidence, n-1, loc=np.mean(vals), scale=stats.sem(vals)))
```

---

## Test Results

### Test 1: Sample Data `[0.1, 0.2, 0.3, 0.4, 0.5]`
| Method | Lower CI | Upper CI |
|--------|----------|----------|
| Method A | 0.1036756838522443 | 0.4963243161477557 |
| Method B | 0.1036756838522443 | 0.4963243161477557 |

**Difference**: 0.0 (identical)

### Test 2: HWIN-VAR-001 Linear Regression R² (recovered stats)
| Parameter | Value |
|-----------|-------|
| Mean | 0.07652779978140505 |
| Recovered Std | 0.02822605358173085 |
| n | 5 |
| t_{0.975, 4} | 2.7764451051977934 |
| SE | 0.012623074909060318 |
| Half-width | 0.0350472745438056 |
| CI | [0.041480525237599444, 0.11157507432521065] |

Both methods produce identical results.

---

## Verification on All 385 Metric Combinations

For each of the 385 metric combinations (11 variables × 7 models × 5 metrics):
1. Recover std from reported CI (n=25)
2. Compute corrected CI using n=5 with both methods
3. Compare results

**Result**: All 385 combinations show **zero difference** between Method A and Method B (absolute difference ≤ 1e-15).

---

## Tolerance Check

**Required tolerance**: absolute difference ≤ 1e-12  
**Actual maximum difference**: 0.0 (well within tolerance)

---

## Conclusion

**Both CI calculation methods are mathematically equivalent and produce identical results.** The CI calculation in the canonical code (Method A) is correct. The only issue is the incorrect sample size (n=25 instead of n=5).