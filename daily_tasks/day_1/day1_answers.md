# Onboarding Day 1: School Incident Analysis - Answers

[Here](https://docs.google.com/spreadsheets/d/1zbQY23ITLgMxgfDk0eIK354g8wK13n6wOKhqZ1ZwDK0/edit?usp=sharing), you can find the Google Sheet document containing the data, cleaned data, and analysis.

## Explore dataset

**Q**: How many total rows are there? 

**A**: *The dataset contains 6,311 rows.*

**Q**: How many unique schools are listed?

**A**: *There are 1890 unique schools listed in the dataset*

**Q**: What is the most frequent incident type?

**A**: *Non-Criminal incidents (NoCrim) are the most frequent incident type with 11,772 incidents.*

**Q**: What % of incidents occurred in the Bronx?

**A**: *28.24% of all incidents occurred in the Bronx.*

## Anomalies

* There is **missing data in several columns**, like **DBN, Register**, and **Building Name**. Other rows have N/A across all incident type fields, resulting in a loss of incident information for those records.

* **Missing DBNs could maybe be reconstructed** using location or building information. Other missing values may need to be omitted or imputed to ensure data accuracy.

* Some entries report **0 incidents or have missing data (N/A) across all incident types**. This could indicate mistakes during data entry or reports of 0 incidents.

## Insights

* The **Bronx** and **Brooklyn** together account for **58% of all reported incidents**, while Staten Island has the fewest reported incidents.

* Overall, **incident frequency decreased** between school years 2013–14 and 2015–16, with all categories showing a decline except non-criminal incidents, which increased slightly.
