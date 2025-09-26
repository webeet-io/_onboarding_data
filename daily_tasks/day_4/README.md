# Day 4: Onboarding task 
## Contents: 
- Project objective
- Deliverables
- Tools & platforms
- Cleaning logic
- Schema and database integration

### Project Objective:
My objective was to evaluate, clean, and integrate the NYC SAT results dataset into an existing PostgreSQL database. 

I inspected and cleaned the dataset in VS Code using Python and then I added it to a table that I created in DBeaver as part of the relational schema. 

I created the table using PostgreSQL and the rest of my work I did using Python. I named the table `isabella_leach_sat_results` and the key columns in my table include the following: 

- `dbn` – unique school code
- `school_name` – name of the school
- `num_of_sat_test_takers`
- `sat_critical_reading_avg_score`
- `sat_math_avg_score`
- `sat_writing_avg_score`
- `internal_school_id`
- `contact_extension`
- `pct_students_tested`
- `academic_tier_rating`

### Deliverables:
* `cleaned_sat_results.csv`
* `sat_modeling.ipynb` 

### Tools & platforms:
- Python on VS Code  in a Jupyter Notebook
- SQL to create the table in DBeaver

### Cleaning logic: 
1. Normalised the column names: 
    1. Lowercase letters, removing blank spaces with ‘_’ and removed special characters.
2. Handled duplicates and typos:
    1. I dropped duplicate rows.
    2. There were2 columns with almost the exact same name with the exception of a typo(`sat_critical_reading_avg_score` and `sat_critical_readng_avg_score`), I ran some code to cross check the 2 columns and found that they  had the exact same values so I dropped the column with the typo.
3. Normalising numeric columns:
    1. Removed non-numeric/special characters from the numeric fields.
4. Checking for mistakes & outliers:
    1. It was advised that the SAT values should be in the range of 200-800 so I wrote code check for outliers and remove them.
    2. I made sure to only include rows where the number of SAT test takers is not negative. 
5. I dropped the columns that are not relevant to the final table/information that is needed.

### Schema & database integration:
Target table and location: `nyc_schools.isabella_leach_sat_results` 

Schema: 
```sql
CREATE TABLE nyc_schools.isabella_leach_sat_results (
    dbn TEXT PRIMARY KEY,
    school_name TEXT,
    num_sat_test_takers BIGINT,
    sat_critical_reading_avg_score BIGINT,
    sat_math_avg_score BIGINT,
    sat_writing_avg_score BIGINT,
    internal_school_id TEXT,
    contact_extension TEXT,
    pct_students_tested NUMERIC,
    academic_tier_rating TEXT
); 
