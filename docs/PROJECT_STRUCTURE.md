# Project Structure Guide

- `notebooks/` — Colab/Jupyter experiments.
- `data/raw/` — original data; do not modify.
- `data/processed/` — cleaned/engineered modeling data.
- `data/external/` — supplementary datasets kept separate by provenance.
- `models/` — trained models, vectorizers and embedding model files.
- `results/` — metrics, plots, confusion matrices and comparison tables.
- `backend/` — FastAPI application.
- `frontend/` — React/Vite application.
- `src/` — reusable Python preprocessing/inference code.
- `tests/` — automated tests.
- `docs/` — methodology, audits and project documentation.
