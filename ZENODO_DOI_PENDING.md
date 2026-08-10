# Zenodo DOI Pending — HWIN-Bench v1.0

**Status**: REQUIRES HUMAN ACTION — Real DOI must be minted via Zenodo deposition

---

## DOI Placeholders in Public Release

The following files contain `zenodo.XXXXXXX` placeholders that must be replaced with the actual Zenodo DOI after deposition:

| File | Location | Placeholder | Replacement |
|------|----------|-------------|-------------|
| `README.md` | Line 5 (badge) | `zenodo.XXXXXXX` | Actual Zenodo DOI |
| `README.md` | Line ~202 (citation) | `10.5281/zenodo.XXXXXXX` | Actual Zenodo DOI |
| `CITATION.cff` | Line 5 (doi) | `10.5281/zenodo.XXXXXXX` | Actual Zenodo DOI |
| `CITATION.cff` | Line 33 (dataset doi) | `10.5281/zenodo.XXXXXXX` | Actual Zenodo DOI |
| `docs/DATA_GUIDE.md` | Line ~229 (citation) | `10.5281/zenodo.XXXXXXX` | Actual Zenodo DOI |
| `licenses/ATTRIBUTION.md` | Line ~140 (citation) | `10.5281/zenodo.XXXXXXX` | Actual Zenodo DOI |

---

## Deposition Process

1. **Create GitHub repository** `HWIN-Bench/HWIN-Bench-v1.0`
2. **Push release package** with Git LFS for large data files
3. **Create GitHub Release** `v1.0.0` with tag
4. **Deposit to Zenodo** via GitHub integration:
   - Go to https://zenodo.org/account/settings/github/
   - Enable repository `HWIN-Bench/HWIN-Bench-v1.0`
   - Trigger deposition for tag `v1.0.0`
5. **Obtain DOI** from Zenodo (format: `10.5281/zenodo.XXXXXXXX`)
6. **Replace all placeholders** with actual DOI
7. **Commit and push** DOI updates
8. **Update Zenodo record** if needed

---

## Files to Update After DOI Minting

| File | Lines to Update |
|------|-----------------|
| `README.md` | DOI badge URL, citation DOI |
| `CITATION.cff` | `doi` field (software), `doi` field (dataset reference) |
| `docs/DATA_GUIDE.md` | Citation DOI |
| `licenses/ATTRIBUTION.md` | Citation DOI |

---

## Expected DOI Format

```
10.5281/zenodo.XXXXXXXX
```

Where `XXXXXXXX` is the 8-digit Zenodo record ID.

---

## Timeline

- **DOI minting**: After GitHub release creation
- **Placeholder replacement**: Within 24 hours of DOI availability
- **Public release announcement**: After all placeholders replaced

---

**Status**: BLOCKED — Requires human action to create GitHub repository, push, create release, and deposit to Zenodo.

**Owner**: Release Engineer  
**Date**: 2026-08-09