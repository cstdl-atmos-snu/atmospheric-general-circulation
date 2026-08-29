# Atmospheric General Circulation

Graduate course, School of Earth and Environmental Sciences, Seoul National University (Fall 2026).

## 👉 Course website: https://cstdl-atmos-snu.github.io/atmospheric-general-circulation/

All lecture slides and notebooks are linked from the website above. Start there.

Textbook: J. M. Wallace, D. S. Battisti, D. W. J. Thompson & D. L. Hartmann, *The Atmospheric General Circulation* (Cambridge University Press).

## What is in this repository

| Folder | Contents |
|---|---|
| `docs/` | The course website (GitHub Pages). `docs/slides/` holds the lecture slides as self-contained HTML files (reveal.js). |
| `notebooks/` | Jupyter notebooks for hands-on analysis of the topics covered in class. Each one can be opened in Google Colab with one click from the website. |
| `scripts/` | Helper functions shared by the notebooks (data access, plotting). |
| `environment.yml` | Conda environment for running the notebooks locally. |

## Running the notebooks

**Option 1 — Google Colab (nothing to install).**
Click the *Open in Colab* link next to a notebook on the course website. The first cell installs the few packages Colab does not ship with.

**Option 2 — On your own computer.**
Install [Miniforge](https://github.com/conda-forge/miniforge), then:

```bash
git clone https://github.com/cstdl-atmos-snu/atmospheric-general-circulation.git
cd atmospheric-general-circulation
conda env create -f environment.yml
conda activate agc
jupyter lab
```

## Data

The early notebooks read monthly climatologies of the NCEP/NCAR Reanalysis directly from NOAA PSL's OPeNDAP server, so no download is needed. Later notebooks that need ERA5 will explain how to obtain the required subsets.

## Viewing the slides

Open them from the course website. Inside a slide deck: `→` / `←` or `Space` to navigate, `F` for full screen, `Esc` for the slide overview, `S` for the speaker view, `?` for all shortcuts.
