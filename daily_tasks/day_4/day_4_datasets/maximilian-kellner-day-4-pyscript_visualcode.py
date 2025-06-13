# check Use psycopg2 or sqlalchemy to connect
from sqlalchemy import create_engine
# connect to your database
# example connection string → replace with your real credentials: (i had an value error before)

#engine = create_engine('postgresql://postgres:myrealpassword@localhost:5432/postgres')


# import pandas
import pandas as pd

# ok visulacode had some utf-8 unicode isssues (thanks ai wouldn't have known how to approach this) let's seeif it rolls now
# yeah having some symbols in the final table instead a fancy sign is acceptable for now this just should work
# load csv

with open('C:/Users/Maxdesk/Documents/GitHub/_onboarding_data/daily_tasks/day_4/day_4_datasets/sat-results.csv', mode='r', encoding='cp1252', errors='replace') as f:
    df = pd.read_csv(f)



# lowercase column names
df.columns = df.columns.str.lower().str.strip().str.replace('.', '').str.replace(' ', '_')

# problems key error when ._ occured so i decided to replace dots with _ it follows a structure and keeps it simple
# show columns and first rows
print(df.columns.tolist())
df.head()

# replace 's' with NaN(not a number) in score columns so it will show later as null which is fine 
# because putting 0 would falsely return the score was 0 and maybe chances could be that we get a reported score later
score_columns = [
    'sat_critical_reading_avg_score',
    'sat_math_avg_score',
    'sat_writing_avg_score'
]

for col in score_columns:
    df[col] = pd.to_numeric(df[col].replace('s', pd.NA), errors='coerce')

# replace those 's' with nan in num of sat test takers
df['num_of_sat_test_takers'] = pd.to_numeric(df['num_of_sat_test_takers'].replace('s', pd.NA), errors='coerce')

# ok by now i first cleaned the structure and then cleaned  invalid sat scores so checkpoint 1 and 2
# next step i will drop unrelated fields (mhm school name can be argued but let's keep it)
df = df.drop(columns=[
    'contact_extension',
    'academic_tier_rating',
    'school_name',
    'internal_school_id',
    'sat_critical_readng_avg_score'
])
# also i learned in pandas when NaN == NaN → False because i wanted to compare the data of the duplicates
#i looked over it and they seem the same i safely dropped the onw with typo
# check data types

print(df.dtypes)
# since we were hinted about inconsistent formatting (eg85%) pct students tested appears as an object/string
# so i won't be usable for future filters so i will change that to float
# also the numeric value is enough , the header already described this col is % so the sign isn't needed and steals dataspace also looks incoherent
df['pct_students_tested'] = df['pct_students_tested'].str.replace('%', '').astype(float)
df['num_of_sat_test_takers'] = df['num_of_sat_test_takers'].astype('Int64')
#i was unsure if i should force all int but then the nan wouldn't always work  so i will use float for most
# not for sat test takers these can never be fractional na here instead  is a worthy workaround imo
# well i don't know anything about sat scores but google helped  with each section (Evidence-Based Reading and Writing and Math) 
# scored on a 200-800 scale according to Yocket at least
# define score columns
score_columns = [
    'sat_critical_reading_avg_score',
    'sat_math_avg_score',
    'sat_writing_avg_score'
]

# set invalid scores (< 200 or > 800) to NaN
for col in score_columns:
    df.loc[(df[col] < 200) | (df[col] > 800), col] = pd.NA

# check missing values
print(df.isnull().sum())

# show first rows again
df.head()
# force all string columns to valid UTF-8 BEFORE inserting
for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].astype(str).str.encode('utf-8', errors='replace').str.decode('utf-8')
# save cleaned dataframe to CSV
df.to_csv('cleaned_sat_results.csv', index=False)

print("Cleaned CSV saved as cleaned_sat_results.csv.")

# append data to sat_scores table
print(df.head())

#df.to_sql('sat_scores', engine, if_exists='append', index=False) #ASDFGQ#FG%AS
#apparently it tried to use my realpw and that was why i always got some unicode error
#now it seems fine i commented out couple lines even don't have my postgres pw that was probably connected to some trahmail i don't even know what happened there

print("Data successfully appended to sat_scores table.")
