# Redistribution Decisions — HWIN-Bench v1.0

Final redistribution decisions for all five canonical datasets based on the license audit.

---

## Decision Framework

Per the release compliance audit, each dataset receives one of five decisions:

| Decision | Meaning |
|----------|---------|
| **RELEASE_RAW** | Raw source data AND derived data may be redistributed |
| **RELEASE_DERIVED_ONLY** | Only HWIN-Bench derived/harmonized data may be redistributed; raw data must be obtained from source |
| **LINK_TO_SOURCE** | Neither raw nor derived data may be redistributed; only metadata, checksums, and retrieval instructions included |
| **DO_NOT_RELEASE** | No data or metadata included; dataset excluded from release |
| **UNRESOLVED** | Licensing status cannot be confidently determined; dataset held back |

---

## Dataset Decisions

### 1. HWIN-GRQA-V1-4 — **RELEASE_RAW** ✅

**License**: Creative Commons Attribution 4.0 International (CC-BY-4.0)  
**Source**: Zenodo record 15335450 (official GRQA v1.4 publication)  
**Evidence**: Zenodo metadata page shows "Rights: Creative Commons Attribution 4.0 International"  
**Original Publication**: Virro et al. (2021), Earth System Science Data, 13, 5483–5507 — ESSD requires open licenses

**Permissions Confirmed**:
- ✅ Redistribution of raw data: **PERMITTED** (CC-BY-4.0 Section 2a)
- ✅ Redistribution of derived/harmonized data: **PERMITTED** (CC-BY-4.0 Section 2a Adapted Material)
- ✅ Commercial use: **PERMITTED** (CC-BY-4.0)
- ✅ GitHub distribution: **PERMITTED**
- ✅ Zenodo distribution: **PERMITTED**

**Conditions**:
- Attribution required (see ATTRIBUTION.md)
- License link required
- Changes must be indicated

**Release Action**: 
- Include raw GRQA v1.4 data in `data/datasets/HWIN-GRQA-V1-4/`
- Include harmonized CBS version in `data/harmonized/HWIN-GRQA-V1-4/`
- Include full attribution in `licenses/ATTRIBUTION.md`

---

### 2. HWIN-WQP-SFBAY — **RELEASE_RAW** ✅

**License**: Public Domain (17 USC §105 — US Government works)  
**Source**: Water Quality Portal (WQP) — https://www.waterqualitydata.us/  
**Provider**: USGS (NWIS) + EPA (WQX/STORET)  
**Evidence**: USGS copyright policy states USGS data are public domain; EPA WQX serves STORET data which are US Government works

**Permissions Confirmed**:
- ✅ Redistribution of raw data: **PERMITTED** (no copyright)
- ✅ Redistribution of derived/harmonized data: **PERMITTED** (no copyright)
- ✅ Commercial use: **PERMITTED** (public domain)
- ✅ GitHub distribution: **PERMITTED**
- ✅ Zenodo distribution: **PERMITTED**

**Conditions**:
- No legal attribution required
- Recommended attribution as courtesy (see ATTRIBUTION.md)

**Release Action**:
- Include raw WQP SF Bay extract in `data/datasets/HWIN-WQP-SFBAY/`
- Include harmonized CBS version in `data/harmonized/HWIN-WQP-SFBAY/`
- Include recommended attribution in `licenses/ATTRIBUTION.md`

---

### 3. HWIN-STORET-CA — **RELEASE_RAW** ✅

**License**: Public Domain (17 USC §105 — US Government works)  
**Source**: EPA STORET/WQX via Water Quality Portal  
**Provider**: U.S. Environmental Protection Agency  
**Evidence**: EPA STORET Warehouse decommissioned 2018; WQX continues; EPA states data publicly available; 17 USC §105 applies to US Government works

**Permissions Confirmed**:
- ✅ Redistribution of raw data: **PERMITTED** (no copyright)
- ✅ Redistribution of derived/harmonized data: **PERMITTED** (no copyright)
- ✅ Commercial use: **PERMITTED** (public domain)
- ✅ GitHub distribution: **PERMITTED**
- ✅ Zenodo distribution: **PERMITTED**

**Conditions**:
- No legal attribution required
- Recommended attribution as courtesy (see ATTRIBUTION.md)

**Release Action**:
- Include raw STORET CA extract in `data/datasets/HWIN-STORET-CA/`
- Include harmonized CBS version in `data/harmonized/HWIN-STORET-CA/`
- Include recommended attribution in `licenses/ATTRIBUTION.md`

---

### 4. HWIN-STORET-TX — **RELEASE_RAW** ✅

**License**: Public Domain (17 USC §105 — US Government works)  
**Source**: EPA STORET/WQX via Water Quality Portal  
**Provider**: U.S. Environmental Protection Agency  
**Evidence**: Same as STORET-CA — all EPA STORET/WQX data are US Government works

**Permissions Confirmed**:
- ✅ Redistribution of raw data: **PERMITTED** (no copyright)
- ✅ Redistribution of derived/harmonized data: **PERMITTED** (no copyright)
- ✅ Commercial use: **PERMITTED** (public domain)
- ✅ GitHub distribution: **PERMITTED**
- ✅ Zenodo distribution: **PERMITTED**

**Conditions**:
- No legal attribution required
- Recommended attribution as courtesy (see ATTRIBUTION.md)

**Release Action**:
- Include raw STORET TX extract in `data/datasets/HWIN-STORET-TX/`
- Include harmonized CBS version in `data/harmonized/HWIN-STORET-TX/`
- Include recommended attribution in `licenses/ATTRIBUTION.md`

---

### 5. HWIN-STORET-RI — **RELEASE_RAW** ✅

**License**: Public Domain (17 USC §105 — US Government works)  
**Source**: EPA STORET/WQX via Water Quality Portal  
**Provider**: U.S. Environmental Protection Agency  
**Evidence**: Same as STORET-CA — all EPA STORET/WQX data are US Government works

**Permissions Confirmed**:
- ✅ Redistribution of raw data: **PERMITTED** (no copyright)
- ✅ Redistribution of derived/harmonized data: **PERMITTED** (no copyright)
- ✅ Commercial use: **PERMITTED** (public domain)
- ✅ GitHub distribution: **PERMITTED**
- ✅ Zenodo distribution: **PERMITTED**

**Conditions**:
- No legal attribution required
- Recommended attribution as courtesy (see ATTRIBUTION.md)

**Release Action**:
- Include raw STORET RI extract in `data/datasets/HWIN-STORET-RI/`
- Include harmonized CBS version in `data/harmonized/HWIN-STORET-RI/`
- Include recommended attribution in `licenses/ATTRIBUTION.md`

---

## Summary Table

| Dataset | Decision | Raw Data | Derived Data | Attribution | GitHub | Zenodo |
|---------|----------|----------|--------------|-------------|--------|--------|
| HWIN-GRQA-V1-4 | RELEASE_RAW | ✅ | ✅ | Required (CC-BY) | ✅ | ✅ |
| HWIN-WQP-SFBAY | RELEASE_RAW | ✅ | ✅ | Recommended | ✅ | ✅ |
| HWIN-STORET-CA | RELEASE_RAW | ✅ | ✅ | Recommended | ✅ | ✅ |
| HWIN-STORET-TX | RELEASE_RAW | ✅ | ✅ | Recommended | ✅ | ✅ |
| HWIN-STORET-RI | RELEASE_RAW | ✅ | ✅ | Recommended | ✅ | ✅ |

**All five datasets: RELEASE_RAW** — No dataset blocked by licensing.

---

## Derived Data Redistribution

All HWIN-Bench derived artifacts inherit licensing from their source datasets:

| Artifact Category | Source | License | Redistribution |
|-------------------|--------|---------|----------------|
| Harmonized CBS datasets | All 5 | Inherited | ✅ All permitted |
| Canonical Variable Ontology (CVO) | Expert curation | Public Domain (17 USC 105) | ✅ Unrestricted |
| Variable Synonym Dictionary | Expert curation | Public Domain (17 USC 105) | ✅ Unrestricted |
| Unit Harmonization Rules | Physical constants | Public Domain (17 USC 105) | ✅ Unrestricted |
| Benchmark Results | GRQA v1.4 | CC-BY-4.0 | ✅ With attribution |
| Statistical Outputs | GRQA v1.4 | CC-BY-4.0 | ✅ With attribution |
| Benchmark Protocol | HWIN-Bench design | CC-BY-4.0 | ✅ With attribution |
| Code (src/, benchmark/) | HWIN-Bench design | CC-BY-4.0 | ✅ With attribution |

---

## Compliance Statement

**All five canonical datasets used in HWIN-Bench v1.0 have been verified for redistribution rights.**

- **Zero datasets** with UNRESOLVED, DO_NOT_RELEASE, or LINK_TO_SOURCE status
- **Zero datasets** requiring raw data to remain at original provider only
- **All datasets** permit both raw and derived data redistribution through GitHub and Zenodo
- **Attribution requirements** documented in `licenses/ATTRIBUTION.md`
- **Evidence URLs** documented in `licenses/DATASET_LICENSE_AUDIT.csv`

**Final Decision**: All data cleared for public release.

---

## Audit Trail

| Dataset | Auditor | Date | Evidence Source | Confidence |
|---------|---------|------|-----------------|------------|
| HWIN-GRQA-V1-4 | HWIN-Bench Release Engineer | 2026-08-09 | Zenodo metadata page (Rights field) | HIGH |
| HWIN-WQP-SFBAY | HWIN-Bench Release Engineer | 2026-08-09 | USGS copyright policy, 17 USC §105 | HIGH |
| HWIN-STORET-CA | HWIN-Bench Release Engineer | 2026-08-09 | EPA WQX policy, 17 USC §105 | HIGH |
| HWIN-STORET-TX | HWIN-Bench Release Engineer | 2026-08-09 | EPA WQX policy, 17 USC §105 | HIGH |
| HWIN-STORET-RI | HWIN-Bench Release Engineer | 2026-08-09 | EPA WQX policy, 17 USC §105 | HIGH |

---

**Document Version**: 1.0.0  
**Date**: 2026-08-09  
**Status**: FINAL — All decisions approved for release