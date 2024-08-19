import pandas as pd
import requests
import sqlite3
import os

# Define the URL and the paths
url = 'https://data.wa.gov/api/views/f6w7-q2d2/rows.csv?accessType=DOWNLOAD'
directory_path = os.path.join('..', 'data')
csv_file_path = os.path.join(directory_path, 'data.csv')
db_file_path = os.path.join(directory_path, 'example.db')

# Check if directory exists
os.makedirs(directory_path, exist_ok=True)

# Download, save and read the CSV 
response = requests.get(url)
with open(csv_file_path, 'wb') as file:
    file.write(response.content)

df = pd.read_csv(csv_file_path)

#Rename columns in the dataframe 
new_column_names = {
    'VIN (1-10)': 'VIN',
    'Postal Code': 'Postal_Code',
    'Electric Vehicle Type': 'EV_Type',
    'Clean Alternative Fuel Vehicle (CAFV) Eligibility': 'CAFV_Eligibility',
    'Electric Range': 'EV_Range',
    'Base MSRP': 'MSRP',
    'Legislative District': 'Legislative_District',
    'Vehicle Location': 'Vehicle_Location',
    'Electric Utility': 'Electric_Utility',
    '2020 Census Tract': 'Census_Tract'
    
}

df.rename(columns=new_column_names, inplace=True)

# Connect and save to the SQL database
conn = sqlite3.connect(db_file_path)
df.to_sql('cars', conn, if_exists='replace', index=False)

# Close the connection
conn.close()

print(f"CSV file saved at: {csv_file_path}")
print(f"SQLite database saved at: {db_file_path}")
