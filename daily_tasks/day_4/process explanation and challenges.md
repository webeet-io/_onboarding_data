**SAT Results Cleaning & Database Integration**

1\. Cleaning Logic  

The raw dataset contained 493 rows and 11 columns. To make it analysis-ready, the following steps were performed:  

1\. Standardized column names  
   \- Renamed from verbose format (e.g., \`"SAT Math Avg. Score"\`) to snake\_case (\`sat\_math\_avg\_score\`).    
   \- This ensures consistency and compatibility with SQL.  

2\. Handled missing values  
   \- Some schools had missing or \`"s"\` entries for SAT scores.    
   \- These were replaced with \`NaN\` and dropped where necessary.  

3\. Data type conversion   
   \- Converted SAT score columns from \`object\` → \`numeric\`.    
   \- Ensured borough/district identifiers remained categorical.  

4\. Final schema creation  
   \- Kept only relevant columns for analysis: school\_id, school\_name, borough, and the 3 SAT subject scores.    
   \- This reduced noise and ensured data integrity.  

2\. Challenges Encountered  

\- Connection to PostgreSQL   
  Initially, the connection failed due to using \`"host"\` placeholder instead of the actual Neon database credentials.    
  Fix: replaced with the full connection string including \`sslmode=require\`.  

\- SQLAlchemy error (\`Not an executable object\`)   
  Fix: wrapped SQL queries with \`text()\` from \`sqlalchemy\`.  

\- Column naming mismatches   
  The original dataset used inconsistent capitalization and spacing.    
  Fix: standardized names before cleaning and plotting.  

3\. SQL Schema & Integration  

The cleaned dataset was uploaded into PostgreSQL under the schema \*\*\`nyc\_schools\`\*\*, in the table:  

\`\`\`sql  
CREATE TABLE nyc\_schools.cleaned\_sat\_results (  
    dbn TEXT PRIMARY KEY,  
    school\_name TEXT,  
    borough TEXT,  
    sat\_math\_avg\_score INTEGER,  
    sat\_critical\_reading\_avg\_score INTEGER,  
    sat\_writing\_avg\_score INTEGER  
);

