## Day 1 – School Incident Analysis

🔗 (https://docs.google.com/spreadsheets/d/16QH__G1zZyaYfCAZohx9u1cheEy6iIpN0P0VldGBh_I/edit?usp=sharing)

### Clean the column names:
- Make all lowercase ✅
- Replace spaces with underscores (_) ✅
- Remove special characters ✅

### Answers:
- Total rows: 6311
- Unique schools:  1848 (counted the unique location_code)
- Most frequent incident type: the non-criminal crimes ( NoCrim N)
    We have those incident types:
      Major N: 1781
      Oth N: 6936
      NoCrim N: 11772
      Prop N: 4482
      Vio N: 3180
- Bronx incident %: 24.67%

### Observations:
- A lots of `N/A` or missing values in incident columns 
- if LOCATION is CONSOLIDATED it should be a boolean column for better understanding 
