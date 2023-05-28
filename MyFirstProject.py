import pandas as pd

# Extract File
data = pd.read_csv('https://maven-datasets.s3.amazonaws.com/Marketing%20Campaigns/marketing_data_preview.csv')

# Tampilkan data
print(data)
