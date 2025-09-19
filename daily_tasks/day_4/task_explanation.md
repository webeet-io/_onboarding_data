# SAT Scores Data Cleaning & Database Integration

## 🗂 Dataset Overview

The dataset contains SAT score records from NYC high schools, including fields like:
	•	dbn, school_name, sat_critical_reading_avg_score, sat_math_avg_score, sat_writing_avg_score
	•	Student testing participation and academic tier ratings

⸻

## ✅ Data Cleaning Logic

- Normalized column headers: Renamed all columns to lowercase, replaced spaces with underscores, and removed special characters for consistency.

- Removed duplicate records: Dropped 15 exact duplicates based on all columns.

- Dropped irrelevant fields

Removed:

	- sat_critical_readng_avg_score (duplicate typo column)

	- internal_school_id and contact_extension (not meaningful for analysis)

- Converted data types: Cast all SAT scores, number of test takers, academic tier rating and percentage of students tested to numeric values.

- Removed invalid SAT scores: Filtered out values outside the valid range of 200 to 800 for SAT scores.

- Handled missing values:

	- Dropped rows with missing dbn, school_name, or all three SAT scores.

	- Retained rows with partial SAT score availability for flexibility.

⸻

## ⚠️ Challenges Encountered

- Inconsistent formatting: pct_students_tested was in string format like "85%" and had to be stripped and converted to float.
- Typo in column name: SAT Critical Readng Avg. Score was redundant and removed.
- Outliers: Several scores were outside SAT’s valid range (e.g., >800), which were cleaned.
- Partial missingness: Some records had SAT math score but no writing or reading score, so decisions had to balance data retention vs. completeness.

## 🗃️ SQL Schema & Integration Strategy

Cleaned data was uploaded to a PostgreSQL database hosted on Neon using `SQLAlchemy` with the `psycopg2` driver.

### ▶️ Upload Logic

```python
df_clean.to_sql(
    name='thofa_tazkia_sat_results',
    con=engine,
    schema='nyc_schools',
    if_exists='replace',
    index=False
)
```

- Creates or replaces the `thofa_tazkia_sat_results` table.
- Uses the `nyc_schools` schema.
- Excludes the DataFrame index.

### 🧱 Final Table Schema

| Column Name                         | Data Type | Description                                           |
|------------------------------------|-----------|-------------------------------------------------------|
| `dbn`                              | TEXT      | Unique identifier for each school                    |
| `school_name`                      | TEXT      | Name of the school                                   |
| `num_of_sat_test_takers`           | FLOAT     | Number of students who took the SAT                 |
| `sat_critical_reading_avg_score`   | FLOAT     | Average SAT Critical Reading score                   |
| `sat_math_avg_score`               | FLOAT     | Average SAT Math score                               |
| `sat_writing_avg_score`            | FLOAT     | Average SAT Writing score                            |
| `pct_students_tested`              | FLOAT     | Percentage of students tested                        |
| `academic_tier_rating`             | FLOAT     | School’s academic tier rating                        |

### 🧩 Integration Notes

- Table can be joined with other datasets using the `dbn` field.
- Percentage fields like `"pct_students_tested"` were converted to float (0–100).
- Redundant or unrelated fields were dropped for clarity and relevance.