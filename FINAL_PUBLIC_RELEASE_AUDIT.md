# Final Adversarial Public-Release Audit — HWIN-Bench v1.0

**Date**: 2026-08-09
**Auditor**: Adversarial Release Audit
**Verdict**: C — PUBLIC RELEASE BLOCKED

## Summary

- Total issues: 10
- Blocking (CRITICAL/HIGH): 4
- Non-blocking (MEDIUM/LOW): 6

## Blocking Issues (Must Fix Before Release)

### ISSUE-001 [HIGH]

**Finding**: DOI placeholders (zenodo.XXXXXXX) present in multiple public-facing files

**Evidence**: README.md, CITATION.cff, DATA_GUIDE.md, ATTRIBUTION.md, LICENSE contain XXXXX placeholders

**Affected Files**: README.md, CITATION.cff, docs/DATA_GUIDE.md, licenses/ATTRIBUTION.md

**Required Action**: Replace XXXXX with actual Zenodo DOI before release

### ISSUE-002 [HIGH]

**Finding**: Dataset metadata files contain [TO_BE_COMPUTED] placeholder checksums

**Evidence**: All 5 dataset.json files have sha256:[TO_BE_COMPUTED] for observations.csv, stations.json, variables.csv

**Affected Files**: All 5 dataset.json files in canonical archive

**Required Action**: Compute and embed actual SHA256 checksums before release

### ISSUE-003 [HIGH]

**Finding**: Public release missing checksums.sha256 manifest file

**Evidence**: data/manifests/checksums.sha256 does not exist in release directory

**Affected Files**: data/manifests/checksums.sha256

**Required Action**: Generate SHA256 manifest for all public data files

### ISSUE-004 [HIGH]

**Finding**: Protocol lists 13 benchmarkable variables but canonical execution only produced results for 11

**Evidence**: Protocol §3.3 table lists 13 variables; canonical results directory contains 11 per-variable result files. Missing: HWIN-VAR-004, HWIN-VAR-005, HWIN-VAR-022, HWIN-VAR-023. Extra: HWIN-VAR-028, HWIN-VAR-031

**Affected Files**: benchmark/protocol/01_HWIN_BENCH_PROTOCOL_v1.0.md, README.md, canonical results

**Required Action**: Document and explain the discrepancy; update protocol or results to align

## Non-Blocking Issues (Documentation Fixes)

### ISSUE-005 [MEDIUM]

**Finding**: CVO file contains 49 variables (HWIN-VAR-001 through HWIN-VAR-049), not 51 as previously claimed

**Evidence**: canonical_variable_ontology.csv has 49 rows (excluding header); HWIN-VAR-050 and HWIN-VAR-051 are missing

**Affected Files**: ontology/canonical_variable_ontology.csv, README.md, DATA_GUIDE.md

**Required Action**: Update documentation to reflect actual 49 variables; clarify if 51 was a typo

### ISSUE-006 [LOW]

**Finding**: dataset.json uses CC0-1.0 for WQP/STORET while license audit says "Public Domain (17 USC 105)"

**Evidence**: All 4 WQP/STORET dataset.json files have license: "CC0-1.0"; DATASET_LICENSE_AUDIT.csv says "Public Domain (17 USC 105)"

**Affected Files**: dataset.json (4 files), DATASET_LICENSE_AUDIT.csv, LICENSE, ATTRIBUTION.md

**Required Action**: Harmonize terminology - either use "CC0-1.0 (public domain dedication)" consistently or "Public Domain (17 USC 105)"

### ISSUE-007 [MEDIUM]

**Finding**: README.md inconsistently references 11 and 13 benchmarkable variables

**Evidence**: README mentions "13" at 6 positions and "11" at 3 positions; protocol claims 13, execution has 11

**Affected Files**: README.md

**Required Action**: Standardize on actual executed count (11) with clear explanation of protocol vs execution difference

### ISSUE-008 [LOW]

**Finding**: Public release data/harmonized, data/datasets, data/metadata directories are empty

**Evidence**: Release package has empty data directories; data expected to be downloaded separately

**Affected Files**: data/harmonized/, data/datasets/, data/metadata/

**Required Action**: Document clearly that data must be downloaded; provide download scripts and checksums

### ISSUE-009 [LOW]

**Finding**: README.md does not explicitly mention "LinearRegression" or "code/" directory in main text

**Evidence**: Search for "LinearRegression" and "code/" in README body text - not found in main sections

**Affected Files**: README.md

**Required Action**: Add explicit mention of 7 baseline models and code availability in README

### ISSUE-010 [LOW]

**Finding**: GRQA observations.csv has fields larger than standard CSV limit (131072 bytes)

**Evidence**: csv.Error: field larger than field limit (131072) when reading GRQA observations.csv

**Affected Files**: data/harmonized/HWIN-GRQA-V1-4/observations.csv (if included)

**Required Action**: Note in documentation that CSV may require special handling for large fields

