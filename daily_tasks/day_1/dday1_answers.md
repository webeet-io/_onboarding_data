## Day 1 – School Incident Analysis

Google sheet Link   https://docs.google.com/spreadsheets/d/11qrp_EUDqZKYvX85DQGHRLR9EJBRva3BgML0GnrYI28/edit?usp=sharing
Findings in google sheet under the "Clean",  last columns

### 📊 Answers
- **Total rows:** 6,309  
- **Unique schools:** 364  
- **Most frequent incident type:** Property (prop_n)  
- **% of incidents in Bronx:** 21.3 %

### 🔍 Observations
- Bronx schools record the highest share of total incidents (~21%).  
- Larger enrollment groups generally have slightly higher incident rates.  
- Some schools such as *P.S. 165 Ida Pos* and *Bronx Leadership* show relatively high incident rates per 100 students.  

---

### 🧩 Formulas Used
- `=COUNTA(A2:A)` → counts total rows  
- `=COUNTA(UNIQUE(L2:L))` → counts unique schools  
- `=SUM(M2:M)` , `=SUM(N2:N)` , `=SUM(O2:O)` , `=SUM(P2:P)` → totals per incident type  
- `=SUMIF(Y2:Y,"BRONX",AM2:AM)/SUM(AM2:AM)` → % of incidents in Bronx  

