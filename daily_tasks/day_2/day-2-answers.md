Day 2 – NYC High School Directory 
My Google Colab Notebook link: https://drive.google.com/file/d/1xiN0_JvfUyBTvOfTv6dOGaOPLYpBDpyN/view?usp=sharing


Answers:
# 2.1 Load the dataset using pandas
df_hsd=pd.read_csv('/content/high-school-directory.csv')

# 2.2 Clean the column names (make lowercase, replace spaces with _, remove special characters)
df_hsd.columns = df_hsd.columns.str.strip().str.lower().str.replace(' ','_')

# 3. Filter the dataset to include only schools located in Brooklyn 
Brooklyn_filtered = df_hsd[df_hsd['borough'] == 'Brooklyn']

# 4.1  How many total schools are in Brooklyn?
Brooklyn_filtered.dbn.nunique()
121

# 4.2 How many offer Grade 9 entry?
Brooklyn_filtered[(Brooklyn_filtered.grade_span_min <= 9) & (Brooklyn_filtered.grade_span_max >=9)].dbn.nunique()
121

# 5. Group and summarize
    #5.1 Count of schools per borough
    df_hsd.groupby('borough')['dbn'].nunique()
    
    Bronx	118
    Brooklyn	121
    Manhattan	106
    Queens	80
    Staten Island	10
    
    #5.2 Average number of students per borough
    df_hsd.groupby('borough')['total_students'].mean()
    
    Bronx	490.406780
    Brooklyn	699.134454
    Manhattan	589.825243
    Queens	1046.644737
    Staten Island	1847.500000

    #5.3 Summary of grade_span_max grouped by borough
    df_hsd.groupby('borough')['grade_span_max'].describe()

        	count  	mean	  std	  min	  25%	  50%	  75%	  max
    borough								
    Bronx	118.0	11.906780	0.369506	9.0	12.0	12.0	12.0	12.0
    Brooklyn	121.0	11.933884	0.381566	9.0	12.0	12.0	12.0	12.0
    Manhattan	106.0	11.877358	0.472135	9.0	12.0	12.0	12.0	12.0
    Queens	80.0	11.825000	0.497462	10.0	12.0	12.0	12.0	12.0
    Staten Island	10.0	12.000000	0.000000	12.0	12.0	12.0	12.0	12.0

  # 6. Create visualizations:
    Bar chart: Number of schools per borough
    unique_school = df_hsd.groupby('borough')['dbn'].nunique().reset_index()
    unique_school

    
      borough	  dbn
    0	Bronx	118
    1	Brooklyn	121
    2	Manhattan	106
    3	Queens	80
    4	Staten Island	10 

    sns.barplot(x='borough', y ='dbn', data= unique_school, palette='pastel')

  # 6. Insights:
  - Brooklyn has the highest number of school comparing with other borough.
  - Staten Island has the highest average number of students.
  - In Staten Island all schools have exactly the same value
  - All boroughs show quartiles of 12.0, which means that at least 75% of the schools in every borough have a value of 12 (if we consider the 75% quartile).
  - The variable (25%	  50%	  75%	  max) has a ceiling effect — most schools hit the top value (12).
  - Only the mean, standard deviation, and min differ, showing that some boroughs (like Manhattan and Queens) have a bit more variability and lower values mixed in.
  - Staten Island is an outlier with no variation at all (std = 0). 
  
