# LP30-DGF Paper Package

This directory contains the current PRL-facing working package.

## Files

| Path | Role |
|---|---|
| `dgf_paper_draft.md` | main manuscript working draft |
| `dgf_supplemental.md` | supplemental material working draft |
| `cover_letter_prl.md` | PRL cover letter draft |
| `scripts/generate_dgf_figures.py` | regenerates all figures and CSV tables |
| `figures/` | generated PNG figures |
| `data/` | generated CSV data |
| `pre_submission_check.md` | checklist status and remaining blockers |

## Reproduce Figures and Tables

Run from this directory:

```powershell
python .\scripts\generate_dgf_figures.py
```

The script writes:

- `figures/fig1_mass_map.png`
- `figures/fig2_dephasing_scale.png`
- `figures/fig3_experimental_gap.png`
- `data/mass_map.csv`
- `data/dephasing_scale.csv`
- `data/experimental_gap.csv`
- `data/dgf_estimates.csv`

## Current Status

The current files are optimized for scientific defensibility, not final APS production.  The next production step is conversion to REVTeX and full reference verification.
