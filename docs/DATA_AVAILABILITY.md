# Data availability and release identity — HWIN-Bench v1.0.4

**Status verified: 2026-10-19.** This page is the canonical instructions for obtaining and verifying the currently released harmonized dataset files.

## Current release route

Use the [HWIN-Bench v1.0.4 GitHub Release](https://github.com/Zakariya-Q/HWIN-Bench/releases/tag/v1.0.4). The release has 15 assets. GitHub's reported asset digests were compared against locally calculated SHA-256 digests; all 15 matched. The documented GRQA observation reassembly was also completed as a round-trip test.

The full harmonized GRQA `observations.csv` is distributed as ten sequential byte chunks from one gzip stream. They are not separate gzip files. Download every part, concatenate in filename order, test the gzip stream, decompress, and verify the resulting CSV hash.

### Bash (Linux, macOS, WSL, Git Bash)

Requirements: GitHub CLI (`gh`), gzip and sha256sum. Authenticate with GitHub CLI if required by your environment.

~~~bash
mkdir -p hwin-grqa-release
gh release download v1.0.4 --repo Zakariya-Q/HWIN-Bench \
  --pattern 'hwin-grqa-v1-4_observations.csv.gz.part-*' --dir hwin-grqa-release
cat hwin-grqa-release/hwin-grqa-v1-4_observations.csv.gz.part-* | gzip -t
cat hwin-grqa-release/hwin-grqa-v1-4_observations.csv.gz.part-* | gzip -dc > observations.csv
sha256sum observations.csv
wc -c -l observations.csv
~~~

### PowerShell alternative

~~~powershell
$repo = 'Zakariya-Q/HWIN-Bench'
$release = 'v1.0.4'
$names = 0..9 | ForEach-Object { 'hwin-grqa-v1-4_observations.csv.gz.part-{0:D2}' -f $_ }
New-Item -ItemType Directory -Force hwin-grqa-release | Out-Null
foreach ($name in $names) { gh release download $release --repo $repo --pattern $name --dir hwin-grqa-release }
$out = [System.IO.File]::Create('observations.csv.gz')
try { foreach ($name in $names) { $bytes = [System.IO.File]::ReadAllBytes((Join-Path 'hwin-grqa-release' $name)); $out.Write($bytes, 0, $bytes.Length) } } finally { $out.Dispose() }
gzip -t observations.csv.gz
gzip -dc observations.csv.gz > observations.csv
Get-FileHash observations.csv -Algorithm SHA256
~~~

### Python alternative

Download all ten assets from the v1.0.4 GitHub Release into a folder named `hwin-grqa-release`, preserving the filenames. Then run:

~~~python
from pathlib import Path
import gzip, hashlib

folder = Path('hwin-grqa-release')
parts = [folder / f'hwin-grqa-v1-4_observations.csv.gz.part-{i:02d}' for i in range(10)]
archive = Path('observations.csv.gz')
with archive.open('wb') as out:
    for part in parts:
        if not part.is_file():
            raise FileNotFoundError(part)
        with part.open('rb') as src:
            while chunk := src.read(1024 * 1024):
                out.write(chunk)
with gzip.open(archive, 'rb') as src, Path('observations.csv').open('wb') as out:
    while chunk := src.read(1024 * 1024):
        out.write(chunk)
h = hashlib.sha256()
with Path('observations.csv').open('rb') as f:
    for chunk in iter(lambda: f.read(1024 * 1024), b''):
        h.update(chunk)
print('bytes:', Path('observations.csv').stat().st_size)
print('sha256:', h.hexdigest())
~~~

## Canonical GRQA output checks

| Property | Expected value |
|---|---|
| SHA-256 of decompressed `observations.csv` | `989e5a6ba07499d81443c8819ef7f1e786fdef8a52661474a2bf5cc4a2ed6f8f` |
| File size | 6,016,295,802 bytes |
| Lines including header | 25,850,908 |
| Observation rows excluding header | 25,850,907 |

The complete documented release rejoin test passed during the release audit and reproduced the expected byte size, line count and SHA-256. After verifying, place the file at `data/harmonized/HWIN-GRQA-V1-4/observations.csv` in the intended repository snapshot to reproduce the historical canonical run.

## Asset inventory

| Release asset | Purpose |
|---|---|
| `hwin-bench-v1.0.4_batch1_repo_and_metadata.tar.gz` | Repository snapshot at commit `a70033d` (not identical to the tree referenced by tag `v1.0.4`) |
| `hwin-grqa-v1-4_observations.csv.gz.part-00` … `part-09` | Ten sequential chunks of the harmonized GRQA observation gzip stream |
| `hwin-grqa-v1-4_stations_variables.tar.gz` | GRQA station/variable and dataset metadata files |
| `HWIN-BENCH_v1.0.4_SHA256_MANIFEST.txt` | Asset checksums |
| `REJOIN_INSTRUCTIONS.md`, `README_BATCHES.md` | Release-provided chunk instructions and scope notes |

GitHub reports 15 assets (ten observation chunks and five additional assets). Verify asset checksums using the release manifest/digests and verify decompressed CSV separately using the canonical hash.

## Repository data and quality status

From the repository root, with Git LFS installed and LFS files materialized, verify checked-in files using:

~~~bash
python code/requirements/verify_checksums.py
~~~

Current measured harmonized-file counts (observation rows exclude the header; station counts refer to unique station IDs present in observations; variable counts are data rows in `variables.csv`):

| Dataset | Observation rows | Unique observed station IDs | Variables file rows |
|---|---:|---:|---:|
| HWIN-GRQA-V1-4 | 25,850,907 | 107,828 | 13 |
| HWIN-WQP-SFBAY | 51,050 | 642 | 18 |
| HWIN-STORET-CA | 172,103 | 48,338 | 22 |
| HWIN-STORET-TX | 210,614 | 4,988 | 22 |
| HWIN-STORET-RI | 2,294 | 95 | 19 |

The four regional datasets in the repository do not fully pass strict CBS validation. The San Francisco Bay observation file has a reduced 8-column schema. See `docs/DATA_QUALITY_VALIDATION_REPORT.md`. A checksum pass demonstrates file-byte consistency with the repository manifest; it does not prove schema compliance or scientific validity.

Some `dataset.json` embedded file checksums and planning-stage counts are stale. The `data/manifests/DATASET_RELEASE_INVENTORY.csv` records the current release checksum values and measured file counts, and documents where metadata still requires repair. Do not treat old `dataset.json` count estimates as current audited counts.

## Source citation and redistribution notes

- The upstream GRQA v1.4 source dataset is [Zenodo record 15335450](https://zenodo.org/records/15335450), with CC-BY-4.0 attribution requirements.
- The GRQA *harmonized HWIN-Bench input* is a derived file, so the source GRQA archive alone is not the exact input used in the released benchmark. Use the GitHub Release chunks and verify the expected file hash.
- Water Quality Portal includes data from many contributing agencies. Do not assume all WQP/STORET-derived records share one blanket license. Review source/contributor-specific terms before redistribution.
- The HWIN-Bench code/documentation license does not replace the original source-data terms.

## Project DOI status

The HWIN-Bench deposit DOI `10.5281/zenodo.21877825` remains **reserved but unpublished** as of 2026-10-19. It is not the active public download route and should not be presented as a resolving identifier. Until the final deposit is published and the DOI resolves, cite the [GitHub repository](https://github.com/Zakariya-Q/HWIN-Bench) or [v1.0.4 release](https://github.com/Zakariya-Q/HWIN-Bench/releases/tag/v1.0.4). The upstream GRQA DOI is a separate identifier.

## Scientific-scope note

The current canonical result bundle contains 11 variables, whereas the frozen v1.0 protocol document states a 13-variable scope. This mismatch remains unresolved. This release/documentation repair does not edit the frozen protocol or numeric benchmark results and does not establish complete protocol compliance.
