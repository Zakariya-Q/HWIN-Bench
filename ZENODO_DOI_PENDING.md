# Zenodo DOI status — HWIN-Bench

**Status checked 2026-10-19:** the project deposit DOI `10.5281/zenodo.21877825` is reserved but the deposit is **unpublished**. It must not be presented as a resolving publication DOI or used as the current data-download location.

## Current public access route

The current public HWIN-Bench maintenance release is [v1.0.4 on GitHub](https://github.com/Zakariya-Q/HWIN-Bench/releases/tag/v1.0.4). The harmonized GRQA observation CSV is distributed there as ten sequential byte chunks. Reassembly and integrity verification instructions are in [`docs/DATA_AVAILABILITY.md`](docs/DATA_AVAILABILITY.md).

The upstream GRQA v1.4 source dataset remains available at [Zenodo record 15335450](https://zenodo.org/records/15335450). This is the upstream source DOI, not the DOI for the HWIN-Bench harmonized release.

## Citation until a project DOI is published

Use the GitHub repository or release URL in project citations and software metadata until the reserved deposit is actually published and the DOI resolves. The project DOI is therefore omitted from `CITATION.cff` and from project BibTeX entries.

Do not enable a DOI badge, add the reserved DOI to citation metadata, or tell users that it resolves until all of the following are true:

1. The intended Zenodo deposit has complete, accurate metadata.
2. The final intended release/data package is uploaded and verified.
3. The deposit is published.
4. The DOI resolves to the public record and the record describes the distributed artifact.

## Release identity note

The v1.0.4 release has 15 uploaded assets. Its repository-snapshot asset represents commit `a70033d`; the annotated `v1.0.4` tag peels to commit `1def10f`. Do not describe the asset snapshot as identical to the tagged tree.

## History

- 2026-10-06: reserved project DOI recorded in the repository; deposit remained unpublished.
- 2026-10-19: GitHub Release v1.0.4 verified as the active public access route; project DOI remains reserved/unpublished.
