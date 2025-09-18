# Day 1 — School Incident Analysis (Sebastian Bangemann)

**Google Sheet:** [LINK ZUM SHEET](https://docs.google.com/spreadsheets/d/1aLdL3B2-2NSRJxSOujMgGl3QZxfmviDFZHhkuVlgXPI/edit?usp=sharing)  

---

## Answers

> **Total rows:** 6310  
> **Unique schools (DBN):** 1890  
> **Most frequent incident type:** NoCrim N (highest count)
> **Total # of incidents:** 28,151
> **Total # of incidents 'Bronx':** 7,949  
> **% of incidents in the Bronx:** 28.24% %  
> **Mean incidents per school (where >0):** 10.4  
> **Standard deviation (where >0):** 14.1  

---
 
## Observations / Insights

> - The Bronx dominates incident counts: 4 of the top 5 locations are in the Bronx.  
> - Distribution is highly skewed: most schools report only a few incidents, while a handful drive the totals upward.  
> - Standard deviation is larger than the mean, confirming strong outliers and long-tail behavior.  

---

## Notes on Method

> - Cleaned headers in Google Sheets (lowercase, spaces → `_`, removed special characters).  
> - Computed `total_incidents` as sum of `major_n`, `oth_n`, `nocrim_n`, `prop_n`, and `vio_n`.  
> - Used Google Sheets `QUERY` functions to group data, rank schools (Top-5), and calculate borough shares.  
> - Calculated summary statistics (mean, standard deviation) on schools with >0 incidents.  