## Day 1 Task - School Incident Analysis

### Link: 
https://docs.google.com/spreadsheets/d/1WsN6WAn41JN4nfIHpJj-evdKwjLuiTvVdt1968FrPiM/edit?usp=sharing

### Answers:
- Total rows (before cleaning): **6311**
- Unique schools: **1890** 
- Most frequent incident type: **nocrim_n** with **11 772** incidents
- Bronx incident percentage: **28.24%**

### Observations:
- Brooklyn has the largest number of schools (4335), the highest amount of registered students (1201214) and the highest amount of criminal incidents (8483) which shows a clear correlation between the size of the student population and the crime rate. The higher the population, the higher the crime count
- Overall the number of registered students have been steadily increasing over the years, however the rate of incidents has decreased by 1.42% between 3013-14 and 2015-16
- In the raw data source, in column 'I' which is the number of registered students, there are 2 anomalies:
  
  1. The data type in column 'I' is not numeric as it includes blank cells and 'N/A' values. As a result you cannot conduct any calculations using the data directly from column 'I' which may cause complications later down the line when performing further analysis. As a fix for this anomaly, I entered a formula into column 'AI' of the same sheet where I replaced the blank and 'N/A' values with 0.
 
  2. "N/A" values in the incident value columns indicates that the incident counts grouped across multiple schools that are in the same location/building. The grouped rows can be identified by the word “consolidated" in columns “D”, “J” and “L” along with a blank value in column “C”. As a result of the groupings, column “I” reports **both individual and total** registered students for these groups, which causes the anomaly that inflates the student counts. 


