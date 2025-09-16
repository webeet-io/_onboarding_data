# Answer to the questions (Day 1 - School Incident Analysis)

1. Download the datasets (Done) 
2. Upload the CSV to Google Sheets.(Done)
3. Link to Google Sheet [View the Google Sheet](https://docs.google.com/spreadsheets/d/1DIzcNSxlzB2cKDN7tTS8CgtEZqfhHjDEhnd593LALn4/edit?usp=sharing)

**Clean the column names:** (Done)

  Make all lowercase
  
  Replace spaces with underscores (_)
  
  Remove special characters
  
**Explore the dataset and answer:**

1.How many total rows are there? (6310)

2.How many unique schools are listed? (1890)

3.What is the most frequent incident type? (no criminal)

4.What % of incidents occurred in the Bronx? (28.24%)

5.Look for 1–2 interesting findings or anomalies worth mentioning.

**📌 Key Insights from Borough Incident Data**

	1.	Brooklyn has the highest number of total incidents (8,483), followed closely by the Bronx (7,949) — indicating these boroughs require more safety resources and monitoring.
 
	2.	“No crime” incidents dominate across all boroughs, especially in Staten Island (48.13%) and Bronx (45.36%), suggesting a high volume of school-related reports that don’t result in criminal activity.
 
	3.	Despite having the lowest total incidents, Staten Island shows a higher percentage (48.13%) of non-criminal reports and a lower share of serious incidents — possibly indicating overreporting of minor issues or a more cautious environment.
 
	4.	In terms of major incidents, Manhattan (7.08%) leads in internal percentage, though Brooklyn contributes the most (31.42%) to the city’s total major incidents — pointing to different kinds of safety concerns.
 
	5.	Violation reports are most prevalent in Brooklyn (30.85%) and Bronx (30.60%), suggesting these boroughs face more behavioral or rule-based issues than others.

**Some anomalies**

**🔍 Missing Values Analysis – Key Insights**

	•	The overall percentage of missing values is very low across most columns (under 1%), which means the dataset is generally well-maintained.
	•	However, two fields show significant data quality issues:
	•	dbn (15.91%) and location_code (15.93%) have high missing value rates — these are key identifiers and should be addressed before any location-based analysis.
	•	building_name has the highest missing rate at 40.51%, indicating that building-level data may be incomplete or inconsistently recorded.
	•	Other location-related fields like postcode, longitude, council_district, and nta also have slight missing values (~0.41–0.60%).

