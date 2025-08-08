# NYC SAT Results — Data Cleaning & Integration

## Overview
This dataset contains SAT performance data for NYC high schools, intended to be integrated into the existing PostgreSQL schema (`nyc_schools`).  
The goal was to evaluate, clean, and prepare the dataset for insertion into a new table:  
`nyc_schools.cleaned_sat_results_anna`.

---

## Original Dataset
**Source file:** `sat_results.csv`  
**Original shape:** `478 rows × 11 columns`

**Original columns:**
- `DBN`
- `SCHOOL NAME`
- `Num of SAT Test Takers`
- `SAT Critical Reading Avg. Score`
- `SAT Math Avg. Score`
- `SAT Writing Avg. Score`
- `SAT Critical Readng Avg. Score` *(duplicate with typo)*
- `internal_school_id`
- `contact_extension`
- `pct_students_tested`
- `academic_tier_rating`

---

## Cleaning Steps

### 1. Remove Redundant / Irrelevant Columns
- Dropped **`SAT Critical Readng Avg. Score`** (typo, 100% identical to `SAT Critical Reading Avg. Score`).
- Dropped **`internal_school_id`** (synthetic ID, not used in joins).
- Dropped **`contact_extension`** (irrelevant for SAT analysis).

---

### 2. Normalize Column Names
- Converted to lowercase and replaced spaces with underscores.  
  Example:
  
---

### 3. Handle Duplicates
- Found **10 duplicated DBNs** where rows were identical → removed duplicates.
- Also removed **fully identical rows** → total rows dropped: **15**.

---

### 4. Clean SAT Score Columns
Columns affected:
- `sat_critical_reading_avg._score`
- `sat_math_avg._score`
- `sat_writing_avg._score`

Steps taken:
1. Removed rows containing placeholder `'s'` values (**57 rows**).
2. Converted scores from strings to integers.
3. Dropped rows with scores outside the valid SAT range (`200–800`).

---

### 5. Final Dataset Shape After SAT Cleaning
From **478 rows** → **416 rows** remaining.

---

### 6. `pct_students_tested`
- Originally stored as strings like `"85%"` or `"N/A"`.
- Converted `"85%"` → `0.85` (float).
- Left `NaN` values as-is to preserve dataset size.

---

### 7. `academic_tier_rating`
- Converted to float.
- Preserved `NaN` values.

---

### 8. Type Conversions
Final column types:

| Column                              | Type     |
|-------------------------------------|----------|
| `dbn`                               | text     |
| `school_name`                       | text     |
| `num_of_sat_test_takers`            | integer  |
| `sat_critical_reading_avg._score`   | integer  |
| `sat_math_avg._score`               | integer  |
| `sat_writing_avg._score`            | integer  |
| `pct_students_tested`               | float    |
| `academic_tier_rating`              | float    |

---

## Output
- **Cleaned CSV:** `cleaned_sat_results_anna.csv`
- **Database Table:** `nyc_schools.cleaned_sat_results_anna`
- Inserted using **SQLAlchemy** with explicit schema definition.

---

## Final Notes
- All cleaning decisions aimed to maintain maximum usable data while removing invalid or duplicate entries.
- `pct_students_tested` and `academic_tier_rating` were kept even with missing values to allow future enrichment.
- SAT score columns strictly validated for numeric range.

