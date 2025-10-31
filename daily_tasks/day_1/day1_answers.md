## 📊 School Safety Data Analysis Report

This report summarizes key statistics and findings from the provided dataset.

---

### 🔢 **Basic Data Statistics**

| Metric | Answer | Notes |
| :--- | :--- | :--- |
| **Total Rows** | **6,310** | Total records in the dataset. |
| **Unique Schools** | **1,890** | Total number of unique school entities listed. |
| **Most Frequent Incident Type** | **nocrim\_n** | This category has the highest total count of incidents: **11,772**. |
| **Incidents in The Bronx (%)** | **28.24%** | Percentage of all incidents that occurred within The Bronx. |

---

### 💡 **Interesting Findings & Anomalies**

| Finding Type | Observation | Significance |
| :--- | :--- | :--- |
| **Extreme Anomaly: Crime Rate** | One school has a total student **register of only 3**, yet it reported **4 incidents** (total of `major_n`, `oth_n`, `nocrim_n`, `prop_n`, `vio_n`). | This represents an **extremely high per-student incident rate**, indicating a potential issue with data entry, classification, or a serious safety problem at a very small location. |

---

### 🔗 **Data Source**

You can review the full dataset and calculations here:

[Google Sheet Data Link](https://docs.google.com/spreadsheets/d/1_Vfm-bJgPJsfThlgo0MAIRe7PJIBy3OKE1J5yobvJlQ/edit?usp=sharing)
