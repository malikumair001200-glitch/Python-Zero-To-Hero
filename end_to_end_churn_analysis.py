# Author: Waqas Manzoor
# Description: SQLite Data Extraction, Cleaning, Feature Engineering, KPI Calculation, 
# Ordinal Encoding, and Exploratory Data Analysis (EDA)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3

# -------------------------------------------------------------------
# 1. Data Ingestion from SQLite Database
# -------------------------------------------------------------------
conn = sqlite3.connect('customer_churn.db.db')
sql_query = """
    SELECT name
    FROM sqlite_master
    WHERE type = 'table'
"""
tables = pd.read_sql(sql_query, conn)

# Extract tables into dynamic global DataFrames
for table_name in tables['name']:
    df = pd.read_sql(f"SELECT * FROM {table_name}", conn)
    globals()[f"df_{table_name}"] = df
    print(f"Created DataFrame: df_{table_name}")

conn.close()

# -------------------------------------------------------------------
# 2. Data Cleaning & Standardization (Customer Table)
# -------------------------------------------------------------------
df_db_customer.rename(columns={'name': 'customer'}, inplace=True)
df_db_customer.drop(columns=['interests', 'pincode'], inplace=True, errors='ignore')

# Date parsing & categorical values standardization
df_db_customer['dob'] = pd.to_datetime(df_db_customer['dob'])
df_db_customer['gender'].replace({'Men': 'Male', 'Women': 'Female'}, inplace=True)

# Impute missing country values using state mapping
state_country_mapping = df_db_customer.dropna(subset=['country']).set_index('state')['country'].to_dict()
df_db_customer['country'] = df_db_customer['country'].fillna(df_db_customer['state']).map(state_country_mapping)

# -------------------------------------------------------------------
# 3. Subscriptions & Support Data Processing
# -------------------------------------------------------------------
date_cols = ['subscription_start_date', 'renewal_date', 'cancellation_date']
df_db_subscription[date_cols] = df_db_subscription[date_cols].apply(pd.to_datetime)

# Create Churn Flag
df_db_subscription['churn_flag'] = np.where(df_db_subscription['cancellation_date'].notna(), 1, 0)

# Cleaning support complaints & deduplication
df_db_support.drop(columns=['col_1', 'comment'], inplace=True, errors='ignore')
df_db_support['complaint_date'] = pd.to_datetime(df_db_support['complaint_date'])
df_db_support['complaint_count'] = df_db_support.groupby('customerid')['customerid'].transform('count')
df_db_support = df_db_support.sort_values('complaint_count').drop_duplicates('customerid', keep='last')

# -------------------------------------------------------------------
# 4. Master Dataset Merging & Export
# -------------------------------------------------------------------
df = (df_db_subscription
      .merge(df_db_customer, on='customerid', how='left')
      .merge(df_db_support, on='customerid', how='left'))

df.to_csv('exported_churn_data.csv', index=False)

# -------------------------------------------------------------------
# 5. Core Business KPIs & Metrics
# -------------------------------------------------------------------
churn_rate = df['churn_flag'].mean() * 100
retention_rate = 100 - churn_rate
arpu = df['monthly_charges'].mean()

print(f"Churn Rate: {round(churn_rate, 2)}%")
print(f"Retention Rate: {round(retention_rate, 2)}%")
print(f"ARPU: {round(arpu, 2)}")

# Churn by Plan Type
churn_by_plan = df.groupby('plan_type')['churn_flag'].mean().mul(100).round(2).reset_index(name='churn_rate_pct')
print("\nChurn Rate by Plan:")
print(churn_by_plan)

# Tenure Calculation
today = pd.Timestamp.today()
df['tenure_day'] = np.where(
    df['cancellation_date'].notna(),
    (df['cancellation_date'] - df['subscription_start_date']).dt.days,
    (today - df['subscription_start_date']).dt.days
)
print(f"Average Tenure (Days): {round(df['tenure_day'].mean(), 0)}")

# Revenue at Risk
revenue_at_risk = df.loc[df['churn_flag'] == 1, 'monthly_charges'].sum()
print(f"Revenue at Risk: ${revenue_at_risk}")

# Escalations & Correlation
df['escalations'] = np.where(df['escalations'] == 'Y', 1, 0)
correlation = df['escalations'].corr(df['churn_flag'])
print(f"Escalation vs Churn Correlation: {round(correlation, 2)}")

# Categorize Churn Risk
conditions = [
    (df['churn_score'] < 50),
    (df['churn_score'] >= 50) & (df['churn_score'] < 70),
    (df['churn_score'] >= 70)
]
choices = ['low', 'med', 'high']
df['churn_risk'] = np.select(conditions, choices, default='unknown')

# -------------------------------------------------------------------
# 6. Ordinal Categorical Encoding & Correlation Heatmap
# -------------------------------------------------------------------
df_visuals = df.copy()
df_encoded = df_visuals[['plan_type', 'contract_type', 'churn_score', 'churn_flag', 'churn_risk', 'escalations']].copy()

order_mappings = {
    'plan_type': ['Basic', 'Standard', 'Premium'],
    'contract_type': ['Monthly', 'Annual'],
    'churn_risk': ['low', 'med', 'high']
}

for col, categories in order_mappings.items():
    df_encoded[col] = pd.Categorical(df_encoded[col], categories=categories, ordered=True).codes

plt.figure(figsize=(8, 5))
sns.heatmap(df_encoded.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Customer Churn Feature Correlation Matrix')
plt.show()

# -------------------------------------------------------------------
# 7. SQLite Operations Practice
# -------------------------------------------------------------------
conn_test = sqlite3.connect('test_database.sqlite')
conn_test.execute("CREATE TABLE IF NOT EXISTS users (first_name TEXT, country TEXT, budget INTEGER)")
conn_test.commit()

cursor = conn_test.cursor()
cursor.execute("""
    INSERT INTO users (first_name, country, budget) VALUES 
        ('umair', 'pakistan', 50000),
        ('Waqas', 'pakistan', 60000),
        ('Asim', 'pakistan', 20000)
""")
conn_test.commit()

df_agg = pd.read_sql("SELECT country, SUM(budget) AS total_budget FROM users GROUP BY country", conn_test)
print("\nSQL Aggregation Results:")
print(df_agg)

conn_test.close()
