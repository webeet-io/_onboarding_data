# 🧠 Day 3 – SQL via Python: NYC School Data Exploration

Welcome to **Day 3**! Today, you’ll learn to run SQL queries from within Python — a powerful combo for analysis, automation, and real-world workflows at Webeet.

---

## 🎯 Task Summary

You’ll be working with a PostgreSQL database containing NYC school data. Your goals:

- Connect to the database using Python
- Write SQL queries and fetch results into `pandas` DataFrames
- Analyze school patterns across boroughs, demographics, and safety metrics
- Submit your findings in a Jupyter Notebook

This reflects how we often work at Webeet — combining data access and analysis in one environment.

---

## 🗃️ Database Tables

You’ll be querying these tables:

- `high_school_directory` – School names, locations, types, programs
- `school_demographics` – Enrollment data, ELL, FRPL, disabilities, etc.
- `school_safety_report` – Reported incidents by type and location

---

## 🔌 Connecting to the Database

Set up your connection using one of the following:

- `sqlalchemy` + `psycopg2`  
- `sqlite3` (if working locally with a SQLite dump)  
- `ipython-sql` (optional)

📘 Use the setup guide in:  
📁 `sources/db_connection_guide.md`

⚠️ Do not hardcode credentials — use `.env` files or environment variables instead!

---

## ✅ What to Do

In your notebook, write and execute SQL queries to answer:

### 🧮 School Distribution
- How many schools are there in each borough?

### 🎓 Language Learners
- What is the average percentage of **English Language Learners (ELL)** per borough?

### 🏫 School Size
- Which 10 schools have the **highest total enrollment**?

### ⚠️ Safety + Poverty
- List schools with **>10 reported incidents** and **>50% of students on free/reduced lunch (FRPL)**

### 🔗 Joining Tables
- Join `school_demographics` and `high_school_directory` to find:
  - Schools in **Queens** where **>20% of students have disabilities**

---

## 📁 What to Submit

1. In your sub-branch (`intern-[your-name]/day-3`), go to:  
   📁 `daily_tasks/day_3/`

2. Add your notebook named:  
   📄 `day3_sql_analysis.ipynb`

3. The notebook should include:
   - Connection setup (safe credentials handling)
   - SQL queries and results
   - Commentary or markdown cells explaining what each query shows
   - Summary of insights

4. Create a **Pull Request** with your work  
5. Comment on the GitHub issue with a link to your PR

---

## 🔗 Related GitHub Issue

Track your work and ask questions here:  
👉 [Day 3 – SQL Practice via Python](https://github.com/webeet-io/_onboarding_data/issues/5)

---

## ⏳ Time Estimate

This task should take about **4–5 hours**, including database setup time.

---

Have fun blending SQL with Python — this is where analysis becomes superpowered! 💥🐍🔗
