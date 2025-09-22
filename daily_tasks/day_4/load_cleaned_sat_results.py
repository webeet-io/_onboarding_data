import os
import pandas as pd
from sqlalchemy import create_engine

# --- Pfade definieren ---
RAW_PATH = "day_4_datasets/sat-results.csv"
CLEANED_PATH = "sat_results_cleaned.csv"

# --- Cleaning/Erstellung der bereinigten CSV falls nicht vorhanden ---
if not os.path.exists(CLEANED_PATH):
    print("Cleaned CSV not found. Creating now...")

    # 1. Load raw data
    df = pd.read_csv(RAW_PATH)

    # 2. Standardize columns
    df.columns = [col.strip().lower().replace(" ", "_").replace(".", "").replace("-", "_") for col in df.columns]

    # 3. Remove duplicate DBNs (keep first)
    df = df.drop_duplicates(subset="dbn", keep="first")

    # 4. Remove or merge duplicate/misspelled columns
    # Drop duplicate reading score if it exists
    if "sat_critical_readng_avg_score" in df.columns:
        df = df.drop(columns=["sat_critical_readng_avg_score"])

    # 5. Convert relevant columns to numeric
    num_cols = [
        'num_of_sat_test_takers',
        'sat_critical_reading_avg_score',
        'sat_math_avg_score',
        'sat_writing_avg_score',
        'academic_tier_rating',
        'pct_students_tested'
    ]
    for col in num_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

    # 6. Drop rows with missing values in essential columns
    essential_cols = [
        'dbn',
        'school_name',
        'num_of_sat_test_takers',
        'sat_critical_reading_avg_score',
        'sat_math_avg_score',
        'sat_writing_avg_score'
    ]
    df = df.dropna(subset=essential_cols)

    # 7. Save cleaned file
    df.to_csv(CLEANED_PATH, index=False)
    print(f"Cleaned CSV created and saved as {CLEANED_PATH}")

else:
    print(f"Cleaned CSV already exists at {CLEANED_PATH}.")

# --- Datenbank-Upload ---

# 1. Load cleaned CSV
df_clean = pd.read_csv(CLEANED_PATH)

# 2. Set up DB connection
db_user = "neondb_owner"
db_pass = "npg_CeS9fJg2azZD"
db_host = "ep-falling-glitter-a5m0j5gk-pooler.us-east-2.aws.neon.tech"
db_port = "5432"
db_name = "neondb"
engine = create_engine(
    f"postgresql+psycopg2://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}?sslmode=require"
)

# 3. Write data to PostgreSQL
table_name = "sat_results"
df_clean.to_sql(table_name, engine, index=False, if_exists="append")  # 'replace' for overwrite

print(f"Data from {CLEANED_PATH} successfully loaded into table '{table_name}' in the PostgreSQL database.")
