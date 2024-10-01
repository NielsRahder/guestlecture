import pandas as pd
import requests
import sqlite3
import os

# Define the URLs and the paths
cars_url = 'https://data.wa.gov/api/views/f6w7-q2d2/rows.csv?accessType=DOWNLOAD'
ticket_url = 'https://corgis-edu.github.io/corgis/datasets/csv/parking_citations/parking_citations.csv'

directory_path = os.path.join(os.getcwd(), '../data')

cars_file_path = os.path.join(directory_path, 'cars_data.csv')
ticket_file_path = os.path.join(directory_path, 'ticket_data.csv')
db_file_path = os.path.join(directory_path, 'example.db')

os.makedirs(directory_path, exist_ok=True)

# Download, save, and read the cars CSV
response = requests.get(cars_url)
with open(cars_file_path, 'wb') as file:
    file.write(response.content)

df_cars = pd.read_csv(cars_file_path)

# Download, save, and read the ticket CSV
response = requests.get(ticket_url)
with open(ticket_file_path, 'wb') as file:
    file.write(response.content)

df_tickets = pd.read_csv(ticket_file_path)

# Rename columns in the cars DataFrame
new_cars_column_names = {
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

# Rename columns in the tickets DataFrame
new_ticket_column_names = {
    "Data.Number Plate": 'Plate',
    "Data.State": 'State',
    "Data.Car.Make": 'Make',
    "Data.Car.Style": 'Style',
    "Data.Car.Color": 'Color',
    "Data.Location": 'Location',
    "Data.Violation": 'Violation',
    "Data.Fine": 'Fine',
    "Date.Year": 'Year',
    "Date.Month": 'Month',
    "Date.Day": 'Day',
    "Date.Time.Hour": 'Hour',
    "Date.Time.Minute": 'Minute'
}

# Apply the new column names
df_cars.rename(columns=new_cars_column_names, inplace=True)
df_tickets.rename(columns=new_ticket_column_names, inplace=True)

# Overwrite the CSV files with the renamed columns
df_cars.to_csv(cars_file_path, index=False)
df_tickets.to_csv(ticket_file_path, index=False)

# Connect and save the renamed DataFrames to the SQL database
conn = sqlite3.connect(db_file_path)
df_cars.to_sql('cars', conn, if_exists='replace', index=False)
df_tickets.to_sql('tickets', conn, if_exists='replace', index=False)

# Close the connection
conn.close()

print(f"Cars CSV file saved at: {cars_file_path}")
print(f"Tickets CSV file saved at: {ticket_file_path}")
print(f"SQLite database saved at: {db_file_path}")
