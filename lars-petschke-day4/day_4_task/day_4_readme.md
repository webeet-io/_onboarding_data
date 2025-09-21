# SAT Results Data Integration – Day 4 Task

## Project Overview

This project demonstrates a full data integration workflow for a real-world SAT results dataset, as part of the Webeet onboarding program.  
The main goal is to clean, validate, and append SAT results to a PostgreSQL database, following professional best practices for reproducibility and clarity.

---

## Folder Structure

- **Raw Data:**  
  - `../day_4_datasets/sat-results.csv` (unchanged, only read)
- **All work & outputs in:**  
  - `day_4_task/`
    - `day_4_data_integration.ipynb` – main notebook for cleaning & exploration
    - `sat_results_cleaned.csv` – cleaned CSV, ready for DB upload
    - `load_cleaned_sat_results.py` – script for uploading to PostgreSQL
    - `day_4_readme.md` – this documentation

---

## Workflow Description

### 1. **Inspect and understand the dataset**
- The raw CSV is loaded in the notebook using  
  `df = pd.read_csv("../day_4_datasets/sat-results.csv")`
- The dataset is inspected for structure, relevant columns, duplicates, and data issues.

### 2. **Select and standardize columns**
- All columns are renamed to a consistent, snake_case format for ease of use.
- The `dbn` column is identified as the relational key to link with other tables.

### 3. **Identify and handle issues**
- Duplicate school entries are removed based on the `dbn` column.
- Duplicate or misspelled columns (e.g., `sat_critical_readng_avg_score`) are merged or dropped as needed.
- SAT score columns and numeric fields are converted to numeric types.
- Non-numeric/invalid values in numeric columns are coerced to NaN and handled.
- Rows with missing values in essential columns (dbn, school_name, SAT scores) are dropped.
- Missing values in optional columns (e.g. `contact_extension`, `pct_students_tested`) are kept as NULL (for DB).

### 4. **Save cleaned output**
- The cleaned DataFrame is saved as  
  `sat_results_cleaned.csv` in the `day_4_task/` folder.

### 5. **Upload to PostgreSQL database**
- The script `load_cleaned_sat_results.py` loads the cleaned CSV and appends it to the `sat_results` table in PostgreSQL.
- Connection parameters are provided at the top of the script.
- If the cleaned CSV does not exist, the script displays an error and exits (to prevent uploading raw/uncleaned data).

---

## Running the Project

1. **Run all cells in `day_4_data_integration.ipynb`**  
   - This will load, clean, and save the data as `sat_results_cleaned.csv` in the task folder.

2. **Check for the output:**  
   - The cleaned CSV should appear as `sat_results_cleaned.csv` in the same folder as the notebook and script.

3. **Upload to the database:**  
   - From inside the `day_4_task/` folder, run:  
     ```
     python load_cleaned_sat_results.py
     ```
   - This will append all data from the cleaned CSV to the target table in your PostgreSQL database.

---

## Cleaning Logic & Decisions

- All non-essential columns with missing data are preserved as NULL for maximum data retention.
- Only rows with full information in key SAT columns are kept.
- Duplicates and typos in column names are programmatically resolved.
- Numeric columns are enforced as numeric types for correct analytics and integration.

---

## Challenges

- Handling duplicates and typos in column names from the raw data.
- Resolving non-numeric values in fields expected to be numeric (e.g. "s" instead of score).
- Ensuring all outputs and scripts conform to the required folder structure for onboarding.

---

## Integration Notes

- The `to_sql()` method is used to upload to the PostgreSQL database, with `if_exists="append"` to add data without overwriting.
- Table schema is inferred from the cleaned DataFrame; for production, consider creating the table schema in advance.
- All outputs and scripts are kept inside the `day_4_task/` folder for clarity and easy review.

---

## Summary

This project demonstrates robust, repeatable, and well-documented data integration, with clear separation between raw data, cleaning, and database upload.  
The workflow can be adapted for future data onboarding tasks or real-world data integration projects.

---

**Contact:**  
For questions, please use the GitHub issue tracker for this project.