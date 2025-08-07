# SAT Scores Data Cleaning and Integration Summary

## Data Cleaning Overview

The SAT scores dataset underwent several important preprocessing steps to ensure quality, consistency and compatibility with the existing NYC Schools database

### Cleaning Logic Steps

1. **Standardizing Column Names**
   - All column names were normalized by:
     ```python
     data.columns = data.columns.str.strip().str.lower().str.replace(" ","_").str.replace(".", "")
     ```
   - This ensures consistency across datasets and simplifies SQL/Python access.

2. **Duplicate and Redundant Column Removal**
   - Removed duplicate rows:
     ```python
     data = data.drop_duplicates()
     ```
   - Dropped a redundant/incorrect column (`sat_critical_readng_avg_score`) likely caused by a typo:
     ```python
     data = data.drop(columns="sat_critical_readng_avg_score")
     ```

3. **Type Conversion**
   - Converted score-related columns from string/object to numeric format (handling coercion of errors):
     ```python
     numeric_col = ['num_of_sat_test_takers', 'sat_critical_reading_avg_score','sat_math_avg_score','sat_writing_avg_score']
     ```
   - Removed the `%` symbol and converted `pct_students_tested` to float:
     ```python
     data["pct_students_tested"] = data["pct_students_tested"].str.replace('%','').astype(float)
     ```

4. **Outlier Handling**
   - SAT scores should be between **200–800**:
     - Rows with scores < 200 were dropped.
     - Scores > 800 were clipped to 800 using:
       ```python
       data["sat_math_avg_score"] = data["sat_math_avg_score"].clip(upper=800)
       ```

5. **Dropped Non-Useful Columns**
   - Removed columns not relevant for integration or analysis:
     ```python
     data = data.drop(columns=["contact_extension", "internal_school_id"])
     ```
---

## SQL Schema & Integration Strategy

- **Schema Used**: `nyc_schools`
- **New Table Added**: `sat_scores_mariia`
- **Integration Key**: All major tables (`sat_scores_mariia`, `high_school_directory`, `school_demographics`, `school_safety_report`) share a common `dbn` (school ID) column.

### Database Upload via SQLAlchemy

The cleaned SAT data was inserted as a **new table** using SQLAlchemy:

```python
data.to_sql(
    name="sat_scores_mariia",
    con=engine,
    schema="nyc_schools",
    if_exists="replace",
    index=False
)
