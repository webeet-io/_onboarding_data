## Data Cleaning Logic

The raw SAT results dataset contained several inconsistencies and formatting issues that required cleaning before integration into the PostgreSQL database.  
The main cleaning steps included:

1. **Standardized column names**  
   Converted all column names to lowercase and snake_case for consistency.

2. **Dropped duplicate rows based on DBN (school identifier)**  
   The dataset originally contained 493 rows but had 15 duplicates.  
   After deduplication, 478 unique schools remained.

3. **Removed duplicate and misspelled columns**  
   The dataset included both `SAT Critical Reading Avg. Score` and a duplicate typo version `SAT Critical Readng Avg. Score`.  
   Only the correctly spelled version was retained.

4. **Converted string-based numeric columns to numeric types**  
   Columns such as:
   - `num_of_sat_test_takers`,
   -`sat_critical_reading_avg_score`
   -`sat_math_avg_score` 
   -`sat_writing_avg_score` 
   -`pct_students_tested`
   were stored as strings. These were converted to integers using `pd.to_numeric(errors='coerce')`.

5. **Removed invalid or out-of-range values**  
   SAT section scores can only range between 200 and 800.  
   Any value outside this range (e.g., `1100` in `sat_math_avg_score`) was replaced with `NaN` to prevent analytical distortion.

6. **Derived total and average scores**    
   - `avg_sat_score` = mean of the three section scores (for exploratory insights)

---

## Challenges 

- **Inconsistent score ranges:**  
  Some schools reported SAT averages above 800, indicating data entry errors.  
  These values were handled using range validation rules.

- **Mixed data formats:**  
  Several numeric columns were stored as strings (sometimes with extra spaces or symbols).  
  Careful conversion was necessary to avoid type errors during the database load.

- **Missing and partial data:**  
  Some schools had missing SAT scores for one or more sections.  
  Instead of dropping these rows, the missing fields were set to `NaN` to maintain school-level completeness.


