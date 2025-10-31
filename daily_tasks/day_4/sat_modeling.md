# SAT Modeling — Cleaning, Challenges, and Integration Notes

## Brief summary of cleaning logic
- Loaded raw `sat-results.csv` into `df_sat` and created a working copy `df_clean`.
- Standardized column names: lowercased, spaces → underscores, removed dots.
- Dropped irrelevant columns (`internal_school_id`, `contact_extension`) and a duplicate typo column when present.
- Handled suppressed values: replaced `'s'` with `NaN` for SAT score and test-taker columns, then converted to numeric.
- Cleaned percentage fields: stripped `%` and whitespace from `pct_students_tested`, converted to numeric.
- Validated SAT score ranges (200–800) and set out-of-range values to `NaN`.
- Converted `num_of_sat_test_takers` to numeric and coerced invalid entries to `NaN`.
- Removed duplicate DBNs (kept first record) and dropped rows missing `dbn`.
- Selected final columns into `df_final`:
  - `dbn`, `school_name`, `num_of_sat_test_takers`, `sat_critical_reading_avg_score`, `sat_math_avg_score`, `sat_writing_avg_score`, `pct_students_tested`, `academic_tier_rating`
- Dropped rows missing any SAT score before insertion and exported cleaned data as `cleaned_sat_results.csv`.

## Key challenges encountered
- Suppressed values represented as `'s'` (text) required explicit replacement and coercion to numeric.
- Percent fields included `%` signs and inconsistent spacing requiring stripping before numeric conversion.
- Duplicate/typo columns (e.g., `SAT Critical Readng Avg. Score`) needed detection and removal to avoid ambiguity.
- Missing values in `academic_tier_rating` and `pct_students_tested` required decisions about imputation vs. keeping as NULL.
- DBN duplicates required deduplication; ensuring DBNs matched the `high_school_directory` table meant filtering to the existing school list before upload.

## SQL schema & integration strategy
- Target table created: `nuzhat_amna_sat_scores` with schema:
  - dbn VARCHAR(10) PRIMARY KEY
  - school_name VARCHAR(255)
  - num_of_sat_test_takers INTEGER
  - sat_critical_reading_avg_score INTEGER
  - sat_math_avg_score INTEGER
  - sat_writing_avg_score INTEGER
  - pct_students_tested DECIMAL(5,2)
  - academic_tier_rating DECIMAL(3,1)
  - created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
  - FOREIGN KEY (dbn) REFERENCES nyc_schools high_school_directory(dbn)