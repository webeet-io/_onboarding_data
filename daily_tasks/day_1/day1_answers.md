1. - 3. View modified file: https://docs.google.com/spreadsheets/d/1YX_9oYnFbcSetnY4ZccH9L3EIdrjeg8ff8gD3P0Q0Zw/edit?usp=sharing
4. - How many total rows are there? 6,311 including column names (COUNTA(A:A) in any column except A)
   - How many unique schools are listed? 2,273 (COUNTA(UNIQUE(D:D)) in any column except D)
   - What is the most frequent incident type? Non-criminal crimes are the most frequent. SUM(M2:M6311) then we apply that until column Q. As O has the highest value of 11,772...
   - What % of incidents occurred in the Bronx? 28.24% OR 7,949/28,151.
     Numerator: =SUMIF(Y:Y, "BRONX", M:M) + SUMIF(Y:Y, "BRONX", N:N) + SUMIF(Y:Y, "BRONX", O:O) + SUMIF(Y:Y, "BRONX", P:P) + SUMIF(Y:Y, "BRONX", Q:Q)
     Denominator: =SUM(M2:Q6311)
5. Findings: BROOKLYN has 8,483 crimes. So with the Bronx it's more than 50% of the criminality.
   Manhattan has less than 20%. Staten Island less than 7% and Queens less than 16%
   
ATTENTION: The formulas I didn't know where to put them so I copied them here...
