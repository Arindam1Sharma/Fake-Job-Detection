# Fake Job Posting Detection

AI/ML project for detecting potentially fraudulent job postings using NLP, semantic embeddings, and neural classification.

## Current Status

- ML data audit and cleaning: Complete
- TF-IDF + Logistic Regression baseline: Complete
- Semantic embeddings: Complete
- Semantic embeddings + MLP: Complete
- Inference pipeline: Working
- FastAPI backend: Planned
- React frontend: Planned
- Deployment: Planned

## Structure

- `notebooks/` — ML experiments
- `data/raw/` — original datasets
- `data/processed/` — cleaned modeling datasets
- `data/external/` — supplementary datasets
- `models/` — trained models and embedding artifacts
- `results/` — metrics and plots
- `backend/` — FastAPI API
- `frontend/` — React/Vite application
- `src/` — reusable Python code
- `tests/` — automated tests
- `docs/` — project documentation

## ML Pipeline

Dataset audit → EDA → TF-IDF baseline → semantic embeddings → MLP classifier → final evaluation → inference pipeline → web application.

The TF-IDF model is retained as the baseline. The semantic MLP is the main model candidate. Because the dataset is highly imbalanced, precision, recall, F1 and PR-AUC are important alongside accuracy.
