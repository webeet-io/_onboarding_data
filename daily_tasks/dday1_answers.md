## Day 1 — School Incident Analysis

[My Google Sheet](https://docs.google.com/spreadsheets/d/1P7o6ysMQtsLTW9XJGf6fUT4RbQLXKUgNnRQW3iQWJeo/edit?usp=sharing)

---

### Answers:

- **Total rows:** 6310  .
- **Unique schools:** 1890  
- **Bronx incident %:** 28.24%  
- **Total incidents (major_n):** 1781  
- **Total incidents (oth_n):** 6936  
- **Total incidents (no_crime):** 11772  
- **Total property crimes:** 4482  
- **Total violent crimes:** 3180  

---

### Geographical Distribution of Incidents

| Borough      | Incidents |
|-------------|-----------|
| Manhattan   | 1247      |
| Brooklyn    | 2044      |
| Queens      | 1189      |
| Bronx       | 1551      |
| Staten Island | 255     |

---

### Observations
- Bronx recorded the **highest share of incidents** (~28.24% of total).
- Brooklyn has the **largest number of schools** represented in the dataset.
- Data was cleaned (lowercase headers, underscores, special chars removed) and derived fields used in pivots (e.g., `borough_name_clean`).
