# 🏫 Day 1 – NYC School Incident Analysis / Exploration
**Objective:** Explore a real-world dataset using Google Sheets, perform simple data cleaning and analysis, and summarize my findings in a Markdown file. 

## 🔗 Data Source
[NYC School Incident Data – Google Sheet](https://docs.google.com/spreadsheets/d/1fWFxYKdvhUIfAWDK6m5W6Ozl79oLoV8z-oe-TNpwErY/edit?gid=1900642373#gid=1900642373)

---

## 🧹 Data Cleaning: Column Name Standardization
To prepare the dataset for analysis, the following cleaning steps were applied to column names:

- All column names were converted to **lowercase**  
- Spaces were replaced with **underscores (`_`)**  
- **Special characters** (e.g., `#`) were removed  

This ensures consistency and makes it easier to reference columns during analysis.

---

## 📊 Data Overview

| **Metric** | **Value** |
|-------------|------------|
| **Total Rows** | 6,310 |
| **Total Columns** | 34 |
| **Unique Schools** | 1,890 |
| **Total Missing Values** | 5,129 (8.1% of all data points) |
| **Most Frequent Incident Type** | Non-criminal incidents (11,772 occurrences, 41.8%) |
| **Bronx Incident Percentage** | 28.2% |

---

## 🔍 Key Findings & Observations

### 1. Borough Concentration: Brooklyn and The Bronx Dominate Incident Reports 🗽
- **Brooklyn** leads with the highest number of incidents: **8,483 (30.1%)**  
- **The Bronx** follows closely with **7,949 (28.2%)**  
- Together, these two boroughs account for **58.3%** of all NYC school incidents.  
- **Staten Island** has the fewest with **1,920 (6.8%)**.

---

### 2. Incident Type Distribution: Non-Criminal Issues Are the Primary Concern ⚠️
- **Non-criminal incidents** (e.g., disorderly conduct, harassment, loitering) are the most frequent type — **11,772 occurrences (41.8%)**.  
- The second-highest category is **“Other” incidents** with **6,936**.  
- Only **17.6%** of incidents are classified as **Major or Violent** combined (4,961 total).  
- This suggests NYC schools deal more with **behavioral and disciplinary** issues rather than serious safety threats.

---

### 3. Uneven Distribution of Serious Incidents 🚨
- **Brooklyn** has the highest rate of serious incidents (**19.2%**).  
- **The Bronx** follows at **18.2%**.  
- **Staten Island** reports the lowest rate (**9.4%**), about half of Brooklyn’s rate.  
- Indicates differing **safety challenges** and **intervention needs** across boroughs.

---

### 4. Data Quality Concerns 🧹
- There are **5,129 missing values** (8.1% of the dataset).  
- Missing entries could lead to **underreported incident rates** if concentrated in certain schools or columns.  

---

## 💡 Insights & Observations
- 🏙 **Brooklyn and The Bronx** require the most attention for safety interventions due to high incident volume and seriousness.  
- ⚖️ The **majority of incidents (41.8%)** are non-criminal, highlighting a need for **behavioral support programs** and **restorative practices** rather than purely punitive measures.  
- 🧩 **Inconsistent reporting** across boroughs may contribute to classification differences, suggesting a need for **standardized data reporting** procedures.

---

**✅ Key Takeaway:**  
While the total number of incidents is high, the predominance of *non-criminal* issues implies that **investing in prevention, behavioral support, and school climate improvements** may be more impactful than focusing solely on security measures.
