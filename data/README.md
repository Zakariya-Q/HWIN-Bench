# Data Files — HWIN-Bench v1.0

This directory contains the currently checked-in harmonized regional datasets and the small metadata files for the canonical GRQA dataset. The full HWIN-Bench GRQA `observations.csv` is distributed separately through the GitHub Release assets.

## Dataset locations

| Dataset | Current observation rows | Distinct station IDs in observations | Rows in variables.csv | Observation payload |
|---|---:|---:|---:|---|
| HWIN-GRQA-V1-4 | 25,850,907 | 107,828 | 13 | [GitHub Release v1.0.4, 10 chunks](https://github.com/Zakariya-Q/HWIN-Bench/releases/tag/v1.0.4) |
| HWIN-WQP-SFBAY | 51,050 | 642 | 18 | In repository tree |
| HWIN-STORET-CA | 172,103 | 48,338 | 22 | In repository tree |
| HWIN-STORET-TX | 210,614 | 4,988 | 22 | In repository tree |
| HWIN-STORET-RI | 2,294 | 95 | 19 | In repository tree |

Counts exclude the CSV header and use distinct station identifiers observed in each observation CSV. They are the measured counts of the current harmonized files, not rounded upstream totals. The GRQA variable catalogue has 13 rows; 11 variables are represented in the current canonical benchmark results. This does not resolve the separate 13-versus-11 scope discrepancy in the frozen protocol.

## Restore the canonical GRQA observations

The v1.0.4 release carries `hwin-grqa-v1-4_observations.csv.gz.part-00` through `part-09`. These are sequential byte ranges of one gzip stream, not ten independent gzip files. Download all parts and concatenate them in filename order.

Run the commands below from a Bash-compatible shell with the GitHub CLI installed:

~~~bash
mkdir -p hwin-grqa-release
gh release download v1.0.4 --repo Zakariya-Q/HWIN-Bench \
  --pattern 'hwin-grqa-v1-4_observations.csv.gz.part-*' --dir hwin-grqa-release
cat hwin-grqa-release/hwin-grqa-v1-4_observations.csv.gz.part-* | gzip -t
cat hwin-grqa-release/hwin-grqa-v1-4_observations.csv.gz.part-* | gzip -dc > observations.csv
sha256sum observations.csv
wc -c -l observations.csv
~~~

Expected verification values:

- SHA-256 of decompressed `observations.csv`: `989e5a6ba07499d81443c8819ef7f1e786fdef8a52661474a2bf5cc4a2ed6f8f`
- File size: 6,016,295,802 bytes
- Line count: 25,850,908 including the header; 25,850,907 observation rows

After verifying the hash, place the reconstructed file at `data/harmonized/HWIN-GRQA-V1-4/observations.csv` in the matching repository snapshot. See [`docs/DATA_AVAILABILITY.md`](../docs/DATA_AVAILABILITY.md) for the release snapshot identity and full access notes.

## Integrity verification

From the repository root, with Git LFS installed and files materialized:

~~~bash
python code/requirements/verify_checksums.py
~~~

`data/manifests/checksums.sha256` covers the checked-in files listed there. The large GRQA observation CSV is a GitHub Release asset, not a normal checked-in file, so verify that reconstructed file separately with the canonical SHA-256 above.

## Data-quality and licensing status

The four regional datasets currently checked into the repository do **not** fully pass strict Canonical Benchmark Schema (CBS) validation. The detailed findings and dataset-specific counts are reported in [`docs/DATA_QUALITY_VALIDATION_REPORT.md`](../docs/DATA_QUALITY_VALIDATION_REPORT.md). Do not describe these datasets as Gold-certified or fully CBS-compliant.

GRQA v1.4 requires attribution under its upstream CC-BY-4.0 license. Water Quality Portal (WQP) aggregates data from multiple contributors; do not assume all WQP/STORET-derived records share a blanket public-domain status. Source-specific redistribution terms require review. See [`licenses/DATASET_LICENSE_AUDIT.csv`](../licenses/DATASET_LICENSE_AUDIT.csv) and [`licenses/ATTRIBUTION.md`](../licenses/ATTRIBUTION.md).

## Related documentation

- [`docs/DATA_AVAILABILITY.md`](../docs/DATA_AVAILABILITY.md): release, download and DOI status
- [`docs/DATA_GUIDE.md`](../docs/DATA_GUIDE.md): datasets, schemas and counts
- [`docs/DATA_PROVENANCE.md`](../docs/DATA_PROVENANCE.md): provenance descriptions
- [`docs/DATA_QUALITY_VALIDATION_REPORT.md`](../docs/DATA_QUALITY_VALIDATION_REPORT.md): strict CBS findings
- [`data/manifests/DATASET_RELEASE_INVENTORY.csv`](manifests/DATASET_RELEASE_INVENTORY.csv): current inventory and checksums
