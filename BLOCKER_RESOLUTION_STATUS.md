# Blocker Resolution Status — HWIN-Bench v1.0 Public Release

> **Historical release-audit record (2026-08).** This document reflects the
> validation state at the time of the original v1.0 release audit. It is
> superseded for current dataset-validation status by
> `docs/DATA_QUALITY_VALIDATION_REPORT.md` (v1.0.2), which documents known CBS
> findings for the shipped datasets. Retained unmodified as audit evidence.

**Date**: 2026-08-09  
**Audit Reference**: FINAL_PUBLIC_RELEASE_AUDIT.md (Verdict: C — BLOCKED)

---

## Blocker Status Summary

| Issue | Description | Status | Resolution |
|-------|-------------|--------|------------|
| **ISSUE-001** | Zenodo DOI placeholders (`zenodo.XXXXXXX`) | **REQUIRES HUMAN ACTION** | Create GitHub repo → push → create release → deposit to Zenodo → mint DOI → replace placeholders |
| **ISSUE-002** | `[TO_BE_COMPUTED]` dataset checksums | **RESOLVED** | All 5 dataset.json files updated with actual SHA-256 checksums |
| **ISSUE-003** | Missing `checksums.sha256` manifest | **RESOLVED** | Generated `data/manifests/checksums.sha256` with 60 entries; verified 59/59 files |
| **ISSUE-004** | Protocol claims 13 variables, execution produced 11 | **RESOLVED (STATE A)** | Forensic analysis confirms canonical 11-variable execution is correct; protocol's 13-variable claim was pre-harmonization estimate |

---

## Detailed Resolution Evidence

### ISSUE-001: Zenodo DOI Placeholders
**Status**: REQUIRES HUMAN ACTION
- **Files affected**: README.md, CITATION.cff, docs/DATA_GUIDE.md, licenses/ATTRIBUTION.md
- **Action required**: Create GitHub repo → push → create release → deposit to Zenodo → mint DOI → replace all `zenodo.XXXXXXX` placeholders
- **Documentation**: ZENODO_DOI_PENDING.md created with replacement locations
- **Blocker type**: Cannot be resolved automatically; requires human Zenodo deposition

### ISSUE-002: Dataset Checksums
**Status**: RESOLVED
- **Files updated**: All 5 dataset.json files in canonical archive and release copy
- **Checksums computed**: SHA-256 for observations.csv, stations.json, variables.csv per dataset
- **Verification**: All checksums match between canonical archive, dataset.json, and manifest

### ISSUE-003: Missing Checksums Manifest
**Status**: RESOLVED
- **File created**: `data/manifests/checksums.sha256` (60 entries)
- **Verification**: 59/59 distributable files verified (1 self-referential entry excluded)
- **Documentation**: CHECKSUM_VERIFICATION.md created with PASS status
- **Self-referential note**: Manifest's own checksum entry is self-referential and correctly excluded from verification

### ISSUE-004: Variable Count Discrepancy (13 vs 11)
**Status**: RESOLVED — STATE A CONFIRMED
- **Forensic analysis**: VARIABLE_ELIGIBILITY_FORENSIC.csv (49 rows, all CVO variables)
- **Root cause**: Protocol §3.3 table represented pre-harmonization estimates
- **Missing 4**: HWIN-VAR-004, 005 (no GRQA mappings); HWIN-VAR-022, 023 (mappings exist but 0 obs after harmonization)
- **Extra 2**: HWIN-VAR-028, 031 correctly auto-selected (≥100 obs in harmonized data)
- **Resolution**: Canonical 11-variable execution is scientifically correct; protocol's 13-variable claim was pre-harmonization estimate
- **Documentation**: ISSUE_004_RESOLUTION_REPORT.md, BENCHMARK_VARIABLE_DEFINITION_v1.0.md

---

## Additional Fixes Completed

### CVO Consistency (Phase 8)
- **Fixed**: README.md and DATA_GUIDE.md now correctly state "49 variables (HWIN-VAR-001 through HWIN-VAR-049)" instead of "51 variables"
- **Actual CVO count**: 49 variables (HWIN-VAR-001 through HWIN-VAR-049)

### Terminology Consistency (Phase 9)
- **Fixed**: All WQP/STORET dataset.json files now use "Public Domain (17 USC 105)" consistently
- **Fixed**: DATASET_LICENSE_AUDIT.csv, ATTRIBUTION.md, REDISTRIBUTION_DECISIONS.md, LICENSE all use consistent terminology
- **Note**: CC0-1.0 is functionally equivalent but legally distinct; standardized on "Public Domain (17 USC 105)"

### README Consistency (Phase 10)
- **Fixed**: "13 benchmarkable variables" → "11 benchmarkable variables" throughout
- **Fixed**: CVO count "51" → "49" throughout
- **Documented**: Clear distinction between CVO universe (49), benchmark-eligible (11), canonically benchmarked (11)

### Documentation Created
1. VARIABLE_ELIGIBILITY_FORENSIC.csv — Complete forensic matrix (49 rows)
2. ISSUE_004_RESOLUTION_REPORT.md — Detailed forensic resolution
3. BENCHMARK_VARIABLE_DEFINITION_v1.0.md — Five-tier variable scope definition
4. CHECKSUM_VERIFICATION.md — Checksum verification report (PASS)
5. ZENODO_DOI_PENDING.md — DOI placeholder tracking
6. BLOCKER_RESOLUTION_STATUS.md — This file

---

## Remaining Actions for Release

### REQUIRES HUMAN ACTION (Cannot automate)
1. **Create GitHub repository** `HWIN-Bench/HWIN-Bench-v1.0`
2. **Configure Git LFS** for large data files (GRQA observations.csv ~6 GB)
3. **Push release package** to GitHub
4. **Create GitHub Release** v1.0.0 with tag
5. **Deposit to Zenodo** via GitHub integration
6. **Mint DOI** and replace all `zenodo.XXXXXXX` placeholders
7. **Announce release**

### RESOLVED (Automated)
- ✅ All dataset checksums computed and embedded
- ✅ Checksums manifest generated and verified
- ✅ Variable count discrepancy resolved (STATE A)
- ✅ CVO count corrected to 49
- ✅ License terminology standardized
- ✅ Variable count standardized to 11
- ✅ All documentation updated and consistent
- ✅ Forensic evidence preserved

---

## Final Release Readiness

| Component | Status |
|-----------|--------|
| Legal/license compliance | ✅ RESOLVED |
| Data integrity | ✅ RESOLVED |
| Variable eligibility | ✅ RESOLVED (STATE A) |
| Checksums | ✅ RESOLVED |
| Documentation consistency | ✅ RESOLVED |
| Zenodo DOI | ⏳ REQUIRES HUMAN ACTION |
| GitHub publication | ⏳ REQUIRES HUMAN ACTION |

---

## Verdict

**Three of four blockers RESOLVED.** One blocker (ISSUE-001: Zenodo DOI) REQUIRES HUMAN ACTION and cannot be automated.

**The release package is scientifically correct, legally compliant, and technically verified.** The remaining step is the standard deposition workflow: GitHub → Zenodo → DOI → placeholder replacement.

**Recommendation**: Proceed with GitHub repository creation and Zenodo deposition. The release package at `HWIN_Bench_v1_PUBLIC_RELEASE/` is ready for publication.

---

**Status Updated**: 2026-08-09  
**Auditor**: Adversarial Release Audit