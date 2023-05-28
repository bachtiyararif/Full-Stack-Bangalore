import datetime
import pandas as pd

# Extract File
data = pd.read_csv('https://maven-datasets.s3.amazonaws.com/Marketing%20Campaigns/marketing_data_preview.csv')

# Transform data
data.columns = data.columns.str.lower()
data.columns = data.columns.str.replace(' ', '')
data['dt_customer'] = pd.to_datetime(data['dt_customer'], format='%Y-%m-%d %H:%M:%S', errors='ignore')

# Add new column 'age'
today = datetime.date.today()
age_cust = today.year - data['year_birth']
data.insert(2, "age", age_cust)

# Tampilkan data
print(data)
