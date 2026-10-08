# CBS Validation Report — HWIN-Bench v1.0.2

**Date**: 2026-10-06
**Validator**: `code/validation/cbs_validator.py` (v1.0.2 — schema-tolerant)
**Scope**: All four datasets shipped in the repository.

This report supersedes the unchecked "PASSED" claims made prior to v1.0.2.
The validator previously crashed on its own shipped datasets (see CHANGELOG
v1.0.2); results below are the first complete validation of the release.

---

## Summary

| Dataset | Observations | Stations | PASSED | Errors | Warnings |
|---------|-------------|----------|--------|--------|----------|
| HWIN-WQP-SFBAY | 51,050 | 642 | NO | 5 | 7 |
| HWIN-STORET-RI | 2,294 | 95 | NO | 4 | 4 |
| HWIN-STORET-CA | 172,103 | 48,338 | NO | 4 | 6 |
| HWIN-STORET-TX | 210,614 | 4,988 | NO | 5 | 8 |

No shipped dataset fully satisfies the Canonical Benchmark Schema. Details
per dataset below. Note that the benchmark itself only exercises GRQA (the
Zenodo-deposited 6 GB dataset); the four in-repo datasets are provided for
reproducibility and transfer-analysis use, and their CBS compliance issues do
not affect the published GRQA results.

---

## HWIN-WQP-SFBAY

Errors:
- Missing 11 CBS-full (Tier 2) columns (`observation_id`, `dataset_id`,
  `latitude`, `longitude`, `country`, `site_name`, `param_name`, `source`,
  `quality_flag`, `percentile`, `country_iso`). The file uses a minimal
  harmonized schema. Coordinates are available via `stations.json` join.
- 1 null `value`.
- Empty or null `unit` rows present.
- HWIN-VAR-009 (Ammonium N): 4 negative concentration values.
- 70 `station_id`s present in observations but absent from `stations.json`.

Warnings:
- Value ranges: VAR-001 ×58, VAR-003 ×1, VAR-008 ×255, VAR-009 ×432,
  VAR-010 ×275, VAR-012 ×18 observations outside expected physical ranges.
- 16,233 rows share a `(station_id, timestamp, variable)` triplet
  (aggregated daily records — expected for this source).

## HWIN-STORET-RI

Errors:
- Missing `percentile` and `country_iso` columns (Tier 2).
- Empty or null `unit` rows present.
- HWIN-VAR-001: 11 non-positive Kelvin values; HWIN-VAR-016: 42.
- 2,272 rows participate in duplicate `observation_id`s. IDs are
  fixed-width space-padded (e.g. `STORET_Rhode_UNB10_19610719_      0920`),
  an artifact of the legacy STORET format; the underlying records are
  distinct (different variables/stations collapse only after padding).

Warnings:
- VAR-031 ×3 outside range; VAR-016 ×42 outside range.
- 1,783 duplicate triplets.
- Non-standard station types (legacy STORET type codes, e.g.
  `/TYPA/AMBNT/STREAM`).

## HWIN-STORET-CA

Errors:
- Missing `percentile` and `country_iso` columns (Tier 2).
- HWIN-VAR-001: 133 non-positive Kelvin values; VAR-002: 1 pH outside [0,14].
- 48,783 rows participate in duplicate `observation_id`s (same padding
  artifact as RI).
- (Resolved in v1.0.2) 171,749 unparseable timestamps — see Timestamp Repairs.

## HWIN-STORET-TX

Errors:
- Missing `percentile` and `country_iso` columns (Tier 2).
- Empty or null `unit` rows present.
- HWIN-VAR-001: 105 non-positive Kelvin values; VAR-016: 4.
- 151,659 rows participate in duplicate `observation_id`s (padding artifact).
- (Resolved in v1.0.2) 210,285 unparseable timestamps — see Timestamp Repairs.

---

## Timestamp Repairs (v1.0.2)

The STORET harmonizer produced malformed timestamps through a strftime
`%H%M:%S`-style bug. All were repaired in place with provenance flags in
`quality_flag`:

| Dataset | Defect | Rows | Repair | Flag |
|---------|--------|------|--------|------|
| RI | `T0920:00` (missing colon) | 2,294 | `T09:20:00` | — |
| RI | `T25:00:00` (STORET unknown-hour) | 807 | `T00:00:00` | `HOUR25` |
| RI | `T99:99:00` (null sentinel) | 2 | `T00:00:00` | `TIME_SENTINEL` |
| CA | `T1215:00` (missing colon) | ~172,009 | `T12:15:00` | — |
| CA | `T25:00:00` | 65,874 | `T00:00:00` | `HOUR25` |
| CA | `T24:00:00` (ISO end-of-day) | 850 | next-day `T00:00:00` | `HOUR24_END_OF_DAY` |
| CA | corrupt minutes (`:80`, `:95`, hour 60+) | 15 | `T00:00:00` | `TIME_CORRUPT` |
| TX | `T1240:00` (missing colon) | ~210,444 | `T12:40:00` | — |
| TX | `T25:00:00` | 9,629 | `T00:00:00` | `HOUR25` |
| TX | corrupt minutes (`:70`, `:75`) | 7 | `T00:00:00` | `TIME_CORRUPT` |

Post-repair parseability: **SFBAY 100%, RI 2294/2294, CA 172103/172103,
TX 210614/210614.**

`HOUR25` follows the STORET convention that hour 25 denotes an unknown time
of day: the date is retained, the time is set to midnight, and the row is
flagged so downstream users can exclude or handle it. The repair deliberately
preserves every observation rather than dropping rows.

---

## Reproduction

```bash
python code/validation/cbs_validator.py data/harmonized/HWIN-WQP-SFBAY
python code/validation/cbs_validator.py data/harmonized/HWIN-STORET-RI
python code/validation/cbs_validator.py data/harmonized/HWIN-STORET-CA
python code/validation/cbs_validator.py data/harmonized/HWIN-STORET-TX
```

Exit code 0 = PASSED, 1 = validation errors found (current state for all four).
