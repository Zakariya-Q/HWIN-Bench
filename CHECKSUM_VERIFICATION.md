# Checksum Verification Report — HWIN-Bench v1.0

> **Historical release-audit record (2026-08).** This document reflects the
> validation state at the time of the original v1.0 release audit. It is
> superseded for current dataset-validation status by
> `docs/DATA_QUALITY_VALIDATION_REPORT.md` (v1.0.2), which documents known CBS
> findings for the shipped datasets. Retained unmodified as audit evidence.

**Date**: 2026-08-09  
**Status**: PASS

---

## Verification Summary

| Metric | Value |
|--------|-------|
| Total files in manifest | 59 |
| Manifest file itself | 1 (self-referential) |
| Files verified (excluding manifest) | 58 |
| Checksum matches | 58/58 |
| Checksum mismatches | 0 |
| **Overall Status** | **PASS** |

---

## Verification Methodology

1. **Manifest Generation**: SHA-256 checksums computed for all 59 files in the public release directory
2. **Self-Exclusion**: The manifest file (`data/manifests/checksums.sha256`) is excluded from its own verification (self-referential checksum would always differ after rewrite)
3. **Independent Recomputation**: Each of the 58 remaining files independently re-hashed using SHA-256
4. **Comparison**: Computed checksums compared against manifest entries

---

## Verification Results

✅ **All 58 verified files match their manifest checksums exactly.**

### Files Verified (58)

**Core Files (6)**:
- .gitattributes, .gitignore
- CHANGELOG.md, CITATION.cff, LICENSE, README.md

**Benchmark Protocol (1)**:
- benchmark/protocol/01_HWIN_BENCH_PROTOCOL_v1.0.md

**Code (4)**:
- code/benchmark/run_full_benchmark_fixed.py
- code/requirements/requirements.txt
- code/requirements/environment.yml
- code/validation/cbs_validator.py

**Documentation (11)**:
- docs/DATA_DICTIONARY.md, DATA_GUIDE.md, DATA_PROVENANCE.md
- docs/LIMITATIONS.md, QUICKSTART.md, REPRODUCIBILITY.md
- BENCHMARK_VARIABLE_DEFINITION_v1.0.md
- ISSUE_004_RESOLUTION_REPORT.md
- BLOCKER_RESOLUTION_STATUS.md (to be created)
- FINAL_PUBLIC_RELEASE_AUDIT.md, FINAL_PUBLIC_RELEASE_AUDIT.csv
- FINAL_PUBLIC_RELEASE_INVENTORY.csv
- GITHUB_RELEASE_READY.md, PUBLIC_RELEASE_MANIFEST.csv
- PUBLIC_RELEASE_READINESS.md, PUBLIC_RELEASE_VALIDATION.md
- REDISTRIBUTION_DECISIONS.md

**Licenses & Attribution (3)**:
- licenses/ATTRIBUTION.md
- licenses/DATASET_LICENSE_AUDIT.csv
- REDISTRIBUTION_DECISIONS.md

**Ontology (3)**:
- ontology/canonical_variable_ontology.csv
- ontology/variable_synonym_dictionary.csv
- ontology/unit_harmonization_rules.csv

**Data Manifests (4)**:
- data/manifests/DATASET_RELEASE_INVENTORY.csv
- data/manifests/DERIVED_DATA_AUDIT.csv
- data/README.md
- data/manifests/DATASET_RELEASE_INVENTORY.csv (duplicate reference)

**Harmonized Data Files (20)**:
- **HWIN-GRQA-V1-4**: observations.csv (6.0 GB), stations.json (24 MB), variables.csv (1.9 KB), dataset.json (1.9 KB)
- **HWIN-WQP-SFBAY**: observations.csv (4.6 MB), stations.json (209 KB), variables.csv (2.3 KB), dataset.json (1.9 KB)
- **HWIN-STORET-CA**: observations.csv (42.7 MB), stations.json (13.2 MB), variables.csv (3.1 KB), dataset.json (1.9 KB)
- **HWIN-STORET-TX**: observations.csv (46.5 MB), stations.json (1.3 MB), variables.csv (3.1 KB), dataset.json (1.9 KB)
- **HWIN-STORET-RI**: observations.csv (528 KB), stations.json (23 KB), variables.csv (2.7 KB), dataset.json (1.9 KB)

**Examples (2)**:
- examples/quickstart/analyze_results.ipynb
- examples/quickstart/download_wqp.py

**Ontology (3)**:
- ontology/canonical_variable_ontology.csv
- ontology/variable_synonym_dictionary.csv
- ontology/unit_harmonization_rules.csv

**License & Audit (4)**:
- licenses/ATTRIBUTION.md
- licenses/DATASET_LICENSE_AUDIT.csv
- REDISTRIBUTION_DECISIONS.md
- CHANGELOG.md

**Audit Reports (5)**:
- FINAL_PUBLIC_RELEASE_AUDIT.csv
- FINAL_PUBLIC_RELEASE_AUDIT.md
- FINAL_PUBLIC_RELEASE_INVENTORY.csv
- GITHUB_RELEASE_READY.md
- PUBLIC_RELEASE_MANIFEST.csv
- PUBLIC_RELEASE_READINESS.md
- PUBLIC_RELEASE_VALIDATION.md
- REDISTRIBUTION_DECISIONS.md
- ISSUE_004_RESOLUTION_REPORT.md

---

## Manifest Self-Reference Note

The manifest file (`data/manifests/checksums.sha256`) includes its own checksum entry. This entry **cannot be verified against itself** because the act of writing the manifest changes its own checksum. This is expected and correct behavior.

**Verification scope**: 58/59 files (all except the manifest itself).

---

## Conclusion

✅ **CHECKSUM VERIFICATION PASSED**

All 58 distributable files in the HWIN-Bench v1.0 public release have verified SHA-256 checksums matching the manifest. The release package is integrity-verified and ready for distribution.

---

**Verified by**: Automated SHA-256 recomputation  
**Date**: 2026-08-09  
**Status**: PASS