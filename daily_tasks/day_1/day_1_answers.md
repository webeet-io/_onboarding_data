# Day 1 – School Incident Analysis

🔗 **[My Google Sheet]([https://docs.google.com/spreadsheets/d/1MmHjvpX1gJ217gLekeJ8pzZklFOZHc_cIO881VA1970/edit?usp=sharing])**

## Dataset Overview
This analysis explores NYC school safety incident data containing information about different types of incidents (non-criminal, property, and violent) across schools in all five boroughs from 2013-2016.

## Data Cleaning Process
Before beginning the analysis, I cleaned the column headers according to the requirements:
- **Made all lowercase:** Converted headers like "School Year" → "school_year"
- **Replaced spaces with underscores:** "Building Code" → "building_code"
- **Removed special characters:** "# Schools" → "schools"

**Method:** Inserted a new row above the original headers, manually entered cleaned names for all 32 columns (A through AF), then deleted the original header row.

---

## Analysis Questions & Solutions

### Question 1: How many total rows are there?

**Approach:** Used Google Sheets COUNTA function to count all non-empty cells in the school_year column, which represents each data record.

**Formula Used:** `=COUNTA(A2:A6311)`

**Explanation:** 
- `A2:A6311` represents the data range (excluding header in A1)
- COUNTA counts all non-empty cells in this range
- Row 1 contains headers, so data starts from row 2

**Result:** **6,310 total rows**

---

### Question 2: How many unique schools are listed?

**Approach:** Used COUNTUNIQUE function on the DBN (District Borough Number) column, as each school has a unique DBN identifier.

**Formula Used:** `=COUNTUNIQUE(C2:C6311)`

**Explanation:**
- Column C contains DBN (District Borough Number) - the unique identifier for each NYC school
- `C2:C6311` covers all data rows excluding the header
- COUNTUNIQUE counts distinct values, giving us the number of unique schools

**Result:** **1,890 unique schools**

---

### Question 3: What is the most frequent incident type?

**Approach:** Since this dataset contains aggregated data rather than individual incident records, I calculated the total count for each incident type across all schools and years.

**Formulas Used:**
- Non-criminal incidents: `=SUM(O2:O6311)` → **11,772**
- Property incidents: `=SUM(P2:P6311)` → **4,482**
- Violent incidents: `=SUM(Q2:Q6311)` → **3,180**

**Explanation:**
- Column O (`nocrim_n`) contains non-criminal incident counts per school
- Column P (`prop_n`) contains property incident counts per school  
- Column Q (`vio_n`) contains violent incident counts per school
- SUM function aggregates all incidents of each type across the entire dataset

**Result:** **Non-criminal incidents** (11,772 total incidents)

---

### Question 4: What % of incidents occurred in the Bronx?

**Approach:** Calculated the percentage of actual incident cases that occurred in the Bronx by summing all incident types for Bronx schools and dividing by the total incidents citywide.

**Formula Used:** `=(SUMIF(Y2:Y6311,"BRONX",O2:O6311)+SUMIF(Y2:Y6311,"BRONX",P2:P6311)+SUMIF(Y2:Y6311,"BRONX",Q2:Q6311))/(SUM(O2:O6311)+SUM(P2:P6311)+SUM(Q2:Q6311))*100`

**Explanation:**
- SUMIF functions calculate total incidents for Bronx schools across all three incident types:
  - Non-criminal incidents: `SUMIF(Y2:Y6311,"BRONX",O2:O6311)`
  - Property incidents: `SUMIF(Y2:Y6311,"BRONX",P2:P6311)`
  - Violent incidents: `SUMIF(Y2:Y6311,"BRONX",Q2:Q6311)`
- Denominator sums all incidents citywide: `SUM(O2:O6311)+SUM(P2:P6311)+SUM(Q2:Q6311)`
- Result shows percentage of actual incident cases, not percentage of schools

**Calculation Breakdown:**
- Total Bronx incidents: 5,594
- Total citywide incidents: 19,434
- Percentage: 5,594 ÷ 19,434 × 100 = 28.78%

**Result:** **28.78% of incidents occurred in the Bronx**

---

## Additional Explorations & Interesting Findings

### Finding 1: Borough Distribution Analysis

**Approach:** Analyzed incident distribution across all five NYC boroughs to identify patterns.

**Formulas Used:**
- Brooklyn: `=COUNTIF(Y2:Y6311,"BROOKLYN")` → **2,044 incidents (32.4%)**
- Bronx: `=COUNTIF(Y2:Y6311,"BRONX")` → **1,550 incidents (24.6%)**
- Manhattan: `=COUNTIF(Y2:Y6311,"MANHATTAN")` → **1,247 incidents (19.8%)**
- Queens: `=COUNTIF(Y2:Y6311,"QUEENS")` → **1,189 incidents (18.8%)**

**Key Insight:** Brooklyn has significantly more incident records than other boroughs - about 32% more than the Bronx, the second-highest borough. This could indicate either higher incident rates or more comprehensive reporting in Brooklyn schools.

### Finding 2: Year-over-Year Trend Analysis

**Approach:** Examined incident trends across the three-year period to identify temporal patterns.

**Formulas Used:**
- 2013-14: `=COUNTIF(A2:A6311,"2013-14")` → **2,159 incidents**
- 2014-15: `=COUNTIF(A2:A6311,"2014-15")` → **2,082 incidents**
- 2015-16: `=COUNTIF(A2:A6311,"2015-16")` → **2,069 incidents**

**Key Insight:** There's a consistent **downward trend** in incident reporting over the three-year period, with approximately 90 fewer incidents recorded each year. This could suggest improving school safety conditions, changes in reporting practices, or enhanced intervention programs.

---

## Summary of Key Findings

### Quantitative Results:
- **Total data records:** 6,310
- **Unique schools represented:** 1,890
- **Most common incident type:** Non-criminal (11,772 total)
- **Bronx representation:** 28.78% of all incidents

### Notable Observations:
- **Geographic disparity:** Brooklyn accounts for nearly one-third of all incident records
- **Positive trend:** Steady annual decrease in reported incidents (2013-2016)
- **Incident type distribution:** Non-criminal incidents are 2.6x more frequent than property incidents and 3.7x more frequent than violent incidents

---

## Technical Notes

**Data Range:** All formulas used the range A2:A6311 (or corresponding columns) to exclude headers and capture the complete dataset.

**Data Quality:** The dataset appears well-structured with consistent formatting, though some calculated averages returned division errors suggesting null values in certain numeric fields.

**Methodology:** Analysis focused on aggregated counts rather than individual incident details, as the dataset structure represents summary statistics per school rather than individual incident records.
