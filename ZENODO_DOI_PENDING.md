# Zenodo DOI Status — HWIN-Bench v1.0

**Status (updated 2026-10-06)**: DOI `10.5281/zenodo.21877825` is **reserved on Zenodo but the deposit is NOT yet published** — the DOI does not resolve yet (Zenodo API: "The persistent identifier is not registered").

**One remaining human step**: log in to Zenodo, open the draft/reserved deposit for `21877825`, complete metadata, upload the release archive, and click **Publish**. Once published, the DOI resolves and the badge below can be enabled.

---

## Current State of DOI References in This Repo

| File | Line | Current value | Status |
|------|------|---------------|--------|
| `CITATION.cff` | 5 | `10.5281/zenodo.21877825` | ✅ Reserved DOI in place — resolves once published |
| `CITATION.cff` | 32 | `10.5281/zenodo.21877825` | ✅ Same reserved DOI (preferred-citation) |
| `README.md` | 8 | Grey "DOI pending" badge | ⏳ Replace with real DOI badge after publishing |
| `README.md` | ~221 | `10.5281/zenodo.21877825` | ✅ BibTeX in README |
| `docs/DATA_GUIDE.md` | citation | `10.5281/zenodo.21877825` | ✅ Reserved DOI in place |
| `licenses/ATTRIBUTION.md` | 140 | `10.5281/zenodo.21877825` | ✅ Reserved DOI in place (fixed 2026-10-06) |

> Note: The GitHub repository lives at `Zakariya-Q/HWIN-Bench`, not the originally
> planned `HWIN-Bench/HWIN-Bench-v1.0` org repo. Citation URLs were corrected accordingly.

---

## How to Finish the Zenodo Publication

1. Go to https://zenodo.org/uploads/21877825 (opens the draft if it belongs to your account)
2. Verify metadata (title, authors, license CC-BY-4.0, keywords)
3. Upload the `HWIN_Bench_v1_PUBLIC_RELEASE/` archive (or connect via the GitHub–Zenodo integration: https://zenodo.org/account/settings/github/ → enable `Zakariya-Q/HWIN-Bench`)
4. Click **Publish**
5. Back here: update the README badge (line 8) from the grey "pending" badge to the real DOI badge:
   `[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.21877825-blue)](https://doi.org/10.5281/zenodo.21877825)`

---

## History

- 2026-08-11: v1.0.0 release package prepared; `zenodo.XXXXXXX` placeholders used pending deposition
- 2026-10-06: Release branch merged to main; reserved DOI `21877825` propagated; invalid ORCID removed from CITATION.cff; attribution URLs corrected to the actual repository
