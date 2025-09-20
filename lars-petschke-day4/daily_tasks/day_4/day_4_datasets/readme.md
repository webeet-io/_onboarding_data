# SAT Results Data Integration – Day 4 Task

## Overview

This project demonstrates a full data integration pipeline for a real-world SAT results dataset.  
The workflow covers raw data inspection, cleaning, schema alignment, and appending the cleaned data to a PostgreSQL database.

## Workflow Summary

1. **Data Inspection:**  
   The original dataset (`sat-results.csv`) was loaded and inspected for structure, relevant columns, and data quality issues.
2. **Column Selection & Standardization:**  
   Columns were renamed for consistency and ease of use. The unique school identifier (`dbn`) was selected as the key for relational integrity.
3. **Data Cleaning:**  
   - Duplicate records (based on `dbn`) were removed.
   - Duplicate/misspelled columns (e.g., `sat_critical_readng_avg_score`) were dropped.
   - SAT score columns and numeric fields were converted to numeric types; invalid or missing values were handled.
   - Rows missing essential information (`dbn`, `school_name`, SAT scores) were removed.
   - Optional columns with missing values were left as NULL (to be stored as NULL in the database).
4. **Export:**  
   The cleaned dataset was saved as `sat_results_cleaned.csv` for reliable database import.
5. **Database Integration:**  
   The provided Python script loads the cleaned CSV and appends the data to the `sat_results` table in the PostgreSQL database using SQLAlchemy.

## Usage

- **Data Cleaning & Export:**  
  Cleaning is performed automatically if `sat_results_cleaned.csv` does not already exist.  
- **Database Upload:**  
  The script reads the cleaned CSV and uploads the data.  
  If the table does not exist, it is created automatically with the correct schema.

## Cleaning Logic

- Key columns were chosen for analysis and database linkage.
- All duplicate and invalid records were removed.
- Data types were strictly enforced for SAT score columns.
- Only complete records (in key fields) are included in the final data.
- The workflow is automated and repeatable for future SAT datasets.

## Challenges

- The raw data contained duplicate and misspelled columns, as well as non-numeric values in numeric fields.
- Some schools appeared more than once with conflicting data, which required manual review or deduplication logic.
- There were missing values in both required and optional fields; a careful approach was used to preserve as much valid data as possible.

## Integration Notes

- The script uses the `to_sql()` function from pandas to insert data into the database.
- Table schema is inferred from the DataFrame; if the structure changes, review and adjust the upload logic.
- For production, further validation and error handling is recommended.

## Files

- `sat-results.csv` (raw data, in `day_4_datasets/`)
- `sat_results_cleaned.csv` (cleaned output, in `day_4_datasets/`)
- `load_cleaned_sat_results.py` (ETL + upload script)
- `day_4_data_integration.ipynb` (analysis and cleaning notebook)
- `day_4_readme.md` (this documentation)

---

**Contact:**  
For any issues or questions, please reach out via the project’s GitHub issue tracker.
