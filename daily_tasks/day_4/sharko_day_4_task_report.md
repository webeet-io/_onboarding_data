# Day 4 Task Report – SAT Results Data Integration

## 1. Cleaning Logic

- **Inspected the dataset**: Viewed the first few rows, checked data types, and identified missing values.
- **Removed duplicates**: Used `drop_duplicates()` to ensure each row is unique.
- **Standardized column names**: Made all column names lowercase and replaced spaces with underscores for consistency.
- **Handled missing values**: Identified columns with missing data and decided whether to fill or drop them (details in notebook).
- **Selected relevant columns**: Focused on columns useful for SAT analysis and those that can be linked to existing tables (e.g., school codes).
- **Explored data**: Used summary statistics and visualizations (histograms, bar charts) to understand distributions and spot outliers.
- **Exported cleaned data**: Saved the cleaned DataFrame as `sharko_cleaned_sat_results.csv` for submission and database loading.

## 2. Challenges Encountered

- Some columns had a high number of missing values, requiring decisions on whether to drop or impute them.
- Data types were inconsistent for some columns (e.g., numeric values stored as strings), which needed conversion.
- Matching school codes/names with existing tables required careful review to ensure relational integrity.
- Understanding the best way to visualize categorical data with many unique values.

## 3. SQL Schema / Integration Notes

- The cleaned data is intended for the `nyc_schools` schema in the PostgreSQL database.
- Table name for import: `sharko_sat_results`.
- Key columns for integration: school code, school name, and SAT score columns.
- If the table structure was adjusted, the new schema was:

```sql
CREATE TABLE nyc_schools.sharko_sat_results (
    school_code VARCHAR,
    school_name VARCHAR,
    sat_math NUMERIC,
    sat_reading NUMERIC,
    sat_writing NUMERIC,
    -- add other relevant columns as needed
);
```
- Data was appended using pandas `.to_sql()` with `if_exists='replace'` to ensure a fresh import.


