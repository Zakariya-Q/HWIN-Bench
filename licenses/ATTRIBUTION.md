# Attribution — HWIN-Bench v1.0

Required attribution for all source datasets used in HWIN-Bench v1.0.

---

## Dataset 1: Global River Water Quality Archive (GRQA) v1.4

**Provider**: Virro, Holger; Amatulli, Giuseppe; Kmoch, Alexander; Shen, Longzhu; Uuemaa, Evelyn  
**License**: Creative Commons Attribution 4.0 International (CC-BY-4.0)  
**License URL**: https://creativecommons.org/licenses/by/4.0/  
**Official Source**: https://zenodo.org/records/15335450  
**DOI**: 10.5281/zenodo.15335450  

### Required Attribution Text (per CC-BY-4.0)
> This work uses data from the Global River Water Quality Archive (GRQA) v1.4 by Virro, H., Amatulli, G., Kmoch, A., Shen, L., & Uuemaa, E. (2025), licensed under CC-BY-4.0. The data was accessed from Zenodo (https://doi.org/10.5281/zenodo.15335450) on 2026-07-08 and harmonized for HWIN-Bench v1.0.

### Required Citation
> Virro, H., Amatulli, G., Kmoch, A., Shen, L., & Uuemaa, E. (2025). Global River Water Quality Archive (GRQA) (Version 1.4) [Dataset]. Zenodo. https://doi.org/10.5281/zenodo.15335450

### Original Publication Citation
> Virro, H., Amatulli, G., Kmoch, A., Shen, L., and Uuemaa, E.: GRQA: Global River Water Quality Archive, Earth Syst. Sci. Data, 13, 5483–5507, https://doi.org/10.5194/essd-13-5483-2021, 2021.

### Attribution Requirements (CC-BY-4.0 Section 3)
When sharing GRQA data or derivatives, you must:
1. Give appropriate credit to the creators
2. Provide a link to the license (https://creativecommons.org/licenses/by/4.0/)
3. Indicate if changes were made
4. Not suggest the licensor endorses you or your use

---

## Dataset 2: USGS/EPA Water Quality Portal — San Francisco Bay Subset

**Provider**: U.S. Geological Survey (USGS) / Environmental Protection Agency (EPA)  
**License**: Public Domain (17 USC §105 — US Government works)  
**Official Source**: https://www.waterqualitydata.us/  
**Access Date**: 2026-07-08  
**Query**: bbox=-123.5,37.0,-121.5,38.5; startDateLo=1950-01-01; startDateHi=2024-12-31; dataSource=NWIS,WQX

### Attribution (Recommended, Not Legally Required)
> Water quality data sourced from the U.S. Geological Survey (USGS) National Water Information System (NWIS) and the Environmental Protection Agency (EPA) Water Quality Exchange (WQX) via the Water Quality Portal (https://www.waterqualitydata.us/), accessed 2026-07-08. USGS and EPA data are in the public domain (17 USC §105).

### Recommended Citation
> U.S. Geological Survey and Environmental Protection Agency. Water Quality Portal. Retrieved 2026-07-08 from https://www.waterqualitydata.us/

### Legal Basis
- USGS data: Public domain under 17 USC §105 (works of the US Government)
- EPA WQX/STORET data: Public domain under 17 USC §105
- WQP integrates both databases; no copyright restrictions apply

---

## Dataset 3: EPA STORET California (HWIN-STORET-CA)

**Provider**: U.S. Environmental Protection Agency (EPA)  
**License**: Public Domain (17 USC §105 — US Government works)  
**Official Source**: https://www.epa.gov/waterdata/storage-and-retrieval-and-water-quality-exchange  
**Access Date**: 2026-07-08  
**Query**: statecode=US:06; startDateLo=1950-01-01; startDateHi=2024-12-31; dataSource=WQX

### Attribution (Recommended, Not Legally Required)
> Water quality data sourced from the U.S. Environmental Protection Agency (EPA) STORET Warehouse / Water Quality Exchange (WQX) via the Water Quality Portal (https://www.waterqualitydata.us/), accessed 2026-07-08. EPA STORET/WQX data are in the public domain (17 USC §105).

### Recommended Citation
> U.S. Environmental Protection Agency. STORET Warehouse / Water Quality Exchange (WQX). Retrieved 2026-07-08 from https://www.epa.gov/waterdata/storage-and-retrieval-and-water-quality-exchange

---

## Dataset 4: EPA STORET Texas (HWIN-STORET-TX)

**Provider**: U.S. Environmental Protection Agency (EPA)  
**License**: Public Domain (17 USC §105 — US Government works)  
**Official Source**: https://www.epa.gov/waterdata/storage-and-retrieval-and-water-quality-exchange  
**Access Date**: 2026-07-08  
**Query**: statecode=US:48; startDateLo=1950-01-01; startDateHi=2024-12-31; dataSource=WQX

### Attribution (Recommended, Not Legally Required)
> Water quality data sourced from the U.S. Environmental Protection Agency (EPA) STORET Warehouse / Water Quality Exchange (WQX) via the Water Quality Portal (https://www.waterqualitydata.us/), accessed 2026-07-08. EPA STORET/WQX data are in the public domain (17 USC §105).

### Recommended Citation
> U.S. Environmental Protection Agency. STORET Warehouse / Water Quality Exchange (WQX). Retrieved 2026-07-08 from https://www.epa.gov/waterdata/storage-and-retrieval-and-water-quality-exchange

---

## Dataset 5: EPA STORET Rhode Island (HWIN-STORET-RI)

**Provider**: U.S. Environmental Protection Agency (EPA)  
**License**: Public Domain (17 USC §105 — US Government works)  
**Official Source**: https://www.epa.gov/waterdata/storage-and-retrieval-and-water-quality-exchange  
**Access Date**: 2026-07-08  
**Query**: statecode=US:44; startDateLo=1950-01-01; startDateHi=2024-12-31; dataSource=WQX

### Attribution (Recommended, Not Legally Required)
> Water quality data sourced from the U.S. Environmental Protection Agency (EPA) STORET Warehouse / Water Quality Exchange (WQX) via the Water Quality Portal (https://www.waterqualitydata.us/), accessed 2026-07-08. EPA STORET/WQX data are in the public domain (17 USC §105).

### Recommended Citation
> U.S. Environmental Protection Agency. STORET Warehouse / Water Quality Exchange (WQX). Retrieved 2026-07-08 from https://www.epa.gov/waterdata/storage-and-retrieval-and-water-quality-exchange

---

## HWIN-Bench Derived Artifacts

The following HWIN-Bench artifacts are derived from the above datasets and inherit their licensing:

| Artifact | Source Dataset(s) | License | Attribution Required |
|----------|-------------------|---------|---------------------|
| Harmonized CBS datasets (`data/harmonized/`) | All 5 | Inherited from source | Yes (per source license) |
| Canonical Variable Ontology (CVO) | Expert curation | Public Domain (17 USC 105) | No |
| Variable Synonym Dictionary | Expert curation | Public Domain (17 USC 105) | No |
| Unit Harmonization Rules | Physical constants | Public Domain (17 USC 105) | No |
| Benchmark Results | GRQA v1.4 | CC-BY-4.0 | Yes (per GRQA license) |
| Statistical Outputs | GRQA v1.4 | CC-BY-4.0 | Yes (per GRQA license) |
| Benchmark Protocol | HWIN-Bench design | CC-BY-4.0 | Yes (per HWIN-Bench license) |

---

## Composite Attribution Statement

When publishing work that uses HWIN-Bench v1.0 data or results, include:

> This work uses HWIN-Bench v1.0 (Heterogeneous Water Quality Intelligence Benchmark), which integrates and harmonizes data from:
> 
> 1. **Global River Water Quality Archive (GRQA) v1.4** — Virro et al. (2025), CC-BY-4.0, https://doi.org/10.5281/zenodo.15335450
> 2. **USGS/EPA Water Quality Portal (WQP)** — San Francisco Bay subset, Public Domain (17 USC §105), https://www.waterqualitydata.us/
> 3. **EPA STORET/WQX** — California, Texas, and Rhode Island subsets, Public Domain (17 USC §105), https://www.epa.gov/waterdata/storage-and-retrieval-and-water-quality-exchange
> 
> HWIN-Bench v1.0 is licensed under CC-BY-4.0. See https://github.com/HWIN-Bench/HWIN-Bench-v1.0 for full attribution and license details.

---

## Citation for HWIN-Bench v1.0

```bibtex
@software{hwin_bench_v1,
  title = {HWIN-Bench v1.0: Heterogeneous Water Quality Intelligence Benchmark},
  author = {HWIN-Bench Consortium},
  year = {2026},
  version = {1.0.0},
  doi = {10.5281/zenodo.XXXXXXX},
  url = {https://github.com/HWIN-Bench/HWIN-Bench-v1.0},
  license = {CC-BY-4.0}
}
```

---

## License Compliance Checklist

When redistributing HWIN-Bench v1.0 or derivatives:

- [ ] Include this ATTRIBUTION.md file
- [ ] Include LICENSE file (CC-BY-4.0 for HWIN-Bench code/docs)
- [ ] For GRQA data: Include CC-BY-4.0 license text and attribution to Virro et al.
- [ ] For WQP/STORET data: Include recommended attribution (not legally required but best practice)
- [ ] Do not imply endorsement by USGS, EPA, or GRQA authors
- [ ] Indicate if you have modified the data
- [ ] Provide link to HWIN-Bench repository

---

## Contact

For attribution questions: hwin-bench@[domain].org or GitHub Issues.

---

**Version**: 1.0.0  
**Last Updated**: 2026-08-09