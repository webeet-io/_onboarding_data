# School Incident Data Exploration

This report summarizes insights from a real-world dataset of school incidents, as part of a data science onboarding task.

---

## ✅ Summary of Key Findings

- **Total Rows in Dataset:** 6,310  
- **Unique Schools (DBN):** 1,931  
- **Unique Locations:** 2,280  
- **Unique (DBN, Location Name) Pairs:** 2,337  
- **Schools Associated with Multiple Locations:** 28  
- **Locations Hosting Multiple Schools:** 53

---

## 🔍 Incident Analysis

- **Most Frequent Incident Type:** `nocrim_n` (Non-criminal incidents)  
- **Percentage of All Incidents Occurring in the Bronx:** 28.38%  
- **Schools with Zero Reported Incidents:** 1,142  
- **Schools with Very High Incident Rates:** See "Top Incident Rates" section in the notebook  
- **Borough-Wise Incident Rates:**  
  While the Bronx has the highest total number of incidents, per-student incident rates across boroughs are closer than expected. Staten Island had the highest per-student rate despite fewer total incidents.

---

## 📌 Interesting Findings


- There are notable outliers in incident rates — both **zero-incident schools** and those with **very high incidents per student**.

- Normalized incident rates across boroughs show **less disparity** than raw totals suggest.

---

## 📎 Resources

- 📄 [Download the cleaned dataset (CSV)](https://drive.google.com/file/d/1tQc2wlfAVOJmsDk-MIjroRWiMi1a1l5V/view?usp=drive_link)  
- 💻 [View the Google Colab notebook](https://colab.research.google.com/drive/147E1ZNGycLHzmd5x7TWxcqwkXquYh81L?usp=sharing)

---

*Prepared as part of a GitHub and data exploration onboarding task.*
