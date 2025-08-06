## Day 1 – School Incident Analysis

https://docs.google.com/spreadsheets/d/1UpamnWI4I3P8mNwxpQj58bP1PGkoxIIj8K-3xwrKHrY/edit?usp=sharing)
https://colab.research.google.com/drive/1eS2xxOphrVDViwJf3h8taTuFtvygKmHM?usp=sharing

    

### Answers:
- Total rows: 6310
  Sheets - =COUNTA(A2:A))
  Python - import pandas as pd
           df = pd.read_csv('/content/Webeet.io_day1 school-safety-repor.csv - school-safety-report.csv')
           total_rows = len(df)
           print('Total Rows:', total_rows)

- Unique schools:
  Here is a tricky point, coz I am still thinking as for exact figure of the unique schools.
Here is my thoughts:
How Many Unique Schools Are in the Dataset?

To estimate the number of unique schools in the dataset, I considered the two most relevant columns:
	1.	DBN (District Borough Number)
	•	A unique 6-character code that identifies each school in NYC.
	•	Result: 1,890 unique DBNs found.
	2.	Address
	•	Represents the physical location (building number and street name) of the school.
	•	Result: 1,212 unique addresses found.

  Interpretation
	•	While addresses can represent shared buildings (e.g., multiple schools co-located in one facility), the DBN is a more precise unit for counting individual schools, as it’s a unique identifier assigned by the NYC Department of Education.
	•	According to NYC DOE’s official 2023–24 data, there are:
	•	1,596 DOE schools
	•	274 charter schools
	•	 Total: ~1,870 schools

Conclusion

The dataset contains 1,890 unique DBNs, which aligns well with the official NYC DOE figure of ~1,870 schools.
Therefore, I consider 1,890 to be the best estimate of the number of unique schools represented in this dataset.


- Most frequent incident type:
  To identify the most frequent type of incident in the dataset, I first looked for a column explicitly named something like "incident_type", but no such column was found.

Instead, the dataset provides aggregated counts of incidents across multiple categories:
	•	major_n –   number of major crimes
	•	oth_n –     number of other crimes
	•	nocrim_n –  number of non-criminal incidents
	•	prop_n –    number of property crimes
	•	vio_n –     number of violent crimes

Analytical Approach

Since the question refers to “incident type” and the dataset contains these numeric columns representing incident counts by category, I infer that these five columns serve as proxy categories for incident types.

To determine the most frequent incident type:
	1.	I computed the sum of each column across all rows.
	2.	I compared the total counts to find the category with the highest cumulative number of reported incidents.

Conclusion

Here we are identified the most frequent incident type by aggregating the total number of occurrences across five predefined crime categories: major_n, oth_n, nocrim_n, prop_n, and vio_n. 
These columns reflect grouped incident types rather than single events.
After summing each column, the one with the highest total represented the most frequently reported incident type in the dataset.

Output: 
Total number of incidents by type:
nocrim_n    11772.0
oth_n        6936.0
prop_n       4482.0
vio_n        3180.0
major_n      1781.0
dtype: float64

Most frequent incident type: 'nocrim_n' with 11772.0 incidents.

  
- Bronx incident %: 6.60% of all incidents occurred in the Bronx.

  To estimate the percentage of incidents occurring in the Bronx, I filtered all records whose DBN string contains the letter "X", as per DOE’s convention (X = Bronx).

I then calculated the sum of all incident columns (major_n, oth_n, nocrim_n, prop_n, vio_n) for both:
	•	the entire dataset, and
	•	the Bronx-only subset.

Finally, I computed the percentage of total Bronx incidents relative to the citywide total.
This approach ensures accuracy even in the absence of a dedicated borough column.

### Observations:

While analyzing the dataset, I discovered:
	1.	A small number of schools (top 1–2%) account for a disproportionately high number of incidents — indicating potential outliers worth further investigation.
	2.	Several schools reported zero incidents across all categories. These may indicate:
	•	underreporting,
	•	truly low-risk environments, or
	•	potential data quality issues.

These findings help flag schools for deeper qualitative investigation or policy focus.
