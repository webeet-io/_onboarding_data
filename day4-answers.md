**Insights**
**For creating the new table 'clara_sat_results' I have dropped the following columns:**

| Column Name                      | Reason to Drop                                   |
| -------------------------------- | ------------------------------------------------ |
| `sat_critical_readng_avg_score`  | Duplicate with typo                              |
| `internal_school_id`             | Not needed (dbn is enough)                       |
| `contact_extension`              | Irrelevant to SAT scores                         |
| `academic_tier_rating`           | Not directly related to SAT performance          |

**The new table 'clara_sat_resuts' contains the folowing columns:**

| Column Name                       | Reason to Keep                                               |
| --------------------------------- | ------------------------------------------------------------ |
| `dbn`                             | Unique school ID — **primary key**                           |
| `school_name`                     | Helpful for identification                                   |
| `num_of_sat_test_takers`          | Important for context (more test takers = more reliable avg) |
| `sat_critical_reading_avg_score`  | Valid SAT component                                          |
| `sat_math_avg_score`              | Valid SAT component                                          |
| `sat_writing_avg_score`           | Valid SAT component                                          |
| `pct_students_tested`             | % of students at the school who took the SAT                 |

Please see the Step 5: Insights in the Jupyter Notebook day4-sat-modeling.jpynb.
