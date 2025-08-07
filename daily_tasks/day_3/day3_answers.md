# 🧠 SQL via Python: NYC School Data Exploration

## 🔌 Project Overview

In this project, we connect to a PostgreSQL database containing NYC school data and execute SQL queries to explore various aspects of high school education in New York City. The analysis covers school demographics, safety reports, and other key metrics.

## 📊 Key Insights

1. **School Distribution**: Brooklyn has the highest number of high schools (121), followed by the Bronx (118), Manhattan (106), Queens (80), and Staten Island (10).

2. **Special Education**: Manhattan schools show the highest average percentage of special education students (26%).

3. **Crime Patterns**: Schools with higher percentages of Hispanic students tend to have higher crime rates, while schools with more Asian and White students show lower crime rates.

4. **English Language Learners**: Manhattan schools have an average of 8% English Language Learners (ELL).

## 🛠️ Technical Setup

### Import Required Libraries

```python
import pandas as pd
import psycopg2
import seaborn as sns
import matplotlib.pyplot as plt
```

### Database Connection

```python
# DB connection setup
conn = psycopg2.connect(
    dbname="neondb",
    user="neondb_owner",
    password="npg_CeS9fJg2azZD",
    host="ep-falling-glitter-a5m0j5gk-pooler.us-east-2.aws.neon.tech",
    port="5432",
    sslmode="require"
)
cur = conn.cursor()
```

## 🔍 Sample Queries

### 1. Count Schools by Borough

```python
query = """
SELECT borough, COUNT(*) AS school_count
FROM nyc_schools.high_school_directory
GROUP BY borough;
"""
df_result = pd.read_sql(query, conn)
df_result
```

### 2. Average ELL Percentage by Borough

```python
query = """
SELECT 
    dir.borough, 
    ROUND(AVG(dem.ell_percent)) || '%' AS avg_ell_percent
FROM nyc_schools.high_school_directory AS dir
INNER JOIN nyc_schools.school_demographics AS dem ON dir.dbn=dem.dbn
GROUP BY dir.borough
"""
df_result = pd.read_sql(query, conn)
df_result
```
<img width="245" height="72" alt="image" src="https://github.com/user-attachments/assets/6cfffb4e-ef33-4355-b9c0-f31cdb9afbe9" />

### 3. Top 3 Schools by Special Education Percentage

```python
query = """
WITH rank_cte AS (
  SELECT dir.borough, dir.dbn, dem.sped_percent, dem.schoolyear,
	ROW_NUMBER () OVER (PARTITION BY dir.borough ORDER BY dem.sped_percent DESC) AS rank
	FROM nyc_schools.high_school_directory AS dir
	INNER JOIN nyc_schools.school_demographics dem ON dem.dbn=dir.dbn
	WHERE 1=1
		AND dem.sped_percent IS NOT NULL
		AND borough IS NOT NULL
		AND dem.sped_percent > 0
  )
 SELECT borough, dbn, sped_percent, schoolyear
 FROM rank_cte
 WHERE rank <4
 ORDER BY borough, sped_percent DESC
"""
df_result = pd.read_sql(query, conn)
df_result
```
<img width="386" height="131" alt="image" src="https://github.com/user-attachments/assets/cbfb3806-8609-4b09-a392-ef50265ef0e0" />

## 📈 Visualizations

### Race Breakdown vs. Crime Rates

```python
query = """
WITH crimes_cte AS (
  SELECT 
    dbn, 
    COALESCE(major_n, 0) 
    + COALESCE(oth_n, 0) 
    + COALESCE(nocrim_n, 0) 
    + COALESCE(prop_n, 0) 
    + COALESCE(vio_n, 0)
    AS n_crimes
  FROM nyc_schools.school_safety_report
),
gender_cte AS (
  SELECT 
      dbn, 
      COALESCE(male_per, 0) AS male_per,
      COALESCE(female_per, 0) AS female_per,
      COALESCE(asian_per, 0) AS asian_per,
      COALESCE(black_per, 0) AS black_per,
      COALESCE(white_per, 0) AS white_per,
      COALESCE(hispanic_per, 0) AS hispanic_per  
    FROM nyc_schools.school_demographics
)
    
SELECT 
    dir.borough, 
    ROUND(AVG(gen.male_per)) AS male_per, 
    ROUND(AVG(gen.female_per)) AS female_per, 
    ROUND(AVG(gen.asian_per)) AS asian_per,
    ROUND(AVG(gen.black_per)) AS black_per,
    ROUND(AVG(gen.white_per)) AS white_per,
    ROUND(AVG(gen.hispanic_per)) AS hispanic_per,
    SUM(cr.n_crimes) AS n_crimes
FROM nyc_schools.high_school_directory dir
INNER JOIN gender_cte AS gen ON gen.dbn = dir.dbn
INNER JOIN crimes_cte AS cr ON cr.dbn = dir.dbn
GROUP BY 1
ORDER BY n_crimes DESC
"""

df_result = pd.read_sql(query, conn)

top10 = df_result.sort_values('n_crimes', ascending=False).head(10)

top10_melted = top10.melt(
    id_vars=['borough', 'n_crimes'],
    value_vars=['male_per', 'female_per', 'asian_per', 'black_per', 'white_per', 'hispanic_per'],
    var_name='group',
    value_name='percentage'
)

plt.figure(figsize=(12, 6))
sns.barplot(data=top10_melted, x='borough', y='percentage', hue='group')
plt.title('Race Breakdown of Top 10 Schools with Most Crimes')
plt.xticks(rotation=0)
plt.ylabel('Percentage (%)')
plt.legend(title='Group')
plt.tight_layout()
plt.show()
```
<img width="1189" height="590" alt="image" src="https://github.com/user-attachments/assets/e53e6da0-192c-4e77-affc-a76a0232b00d" />

## 🏫 Data Sources

- **High School Directory**: Contains basic information about each school
- **School Demographics**: Includes student demographic data
- **School Safety Report**: Contains crime and safety statistics

## 📝 Conclusion

This analysis provides valuable insights into NYC high schools, revealing patterns in school distribution, special education needs, and safety metrics. The visualizations help identify correlations between demographic factors and school performance metrics.
