# Fake Job Scam Detection — Refined Data Pack

## Files

### 1. `fake_job_core_clean.csv`
Primary supervised dataset.

- Rows after cleaning/deduplication: 15,870
- Labels:
  - Legitimate (0): 15,159
  - Fraudulent (1): 711
- Contains the original structured job fields plus:
  - `structured_text`
  - missing-value indicator columns
  - `content_hash`

**Recommended use:** primary training/validation/test construction.

### 2. `secondary_labeled_text_nonoverlap.csv`
Text-only labeled data from the uploaded JSONL splits.

- Rows after exact deduplication and overlap removal: 12,974
- Kept separate because its provenance appears related to the same historical fraud corpus.

**Recommended use:** supplementary robustness experiment, not blindly merged into the main dataset.

### 3. `internship_scam_supplementary.csv`
900-row internship-focused dataset.

**Important:** it substantially overlaps the primary dataset, so it should not be merged into training.

**Recommended use:** specialized internship-scam evaluation/analysis.

### 4. `modern_remote_jobs_unlabeled.csv`
50 recent remote-job examples.

**Important:** there is no verified fraud label. Do not assign `fraudulent=0`.

**Recommended use:** modern-language sanity checks and later feature/URL pipeline testing.

## Excluded

`Unconfirmed 456449.crdownload` was not used because it is an incomplete download.

## Recommended next step

1. Build a leakage-safe train/validation/test split from `fake_job_core_clean.csv`.
2. Preserve the fraud/legitimate ratio with stratification.
3. Keep all duplicate/near-duplicate groups in the same split.
4. Establish a TF-IDF baseline.
5. Train/evaluate the semantic-embedding approach.
6. Use the modern unlabeled data only for domain/robustness experiments unless reliable labels are obtained.
