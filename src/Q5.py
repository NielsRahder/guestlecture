### Q5 ###
## Which car brand has the most amount of tickets in August 2020? 

import pandas as pd
import os
import sqlite3

# Define the path to the SQLite database
db_file_path = os.path.join('data', 'example.db')

# Connect to the SQLite database
conn = sqlite3.connect(db_file_path)

# Your SQL query goes here
query = """
Your answer goes here
"""

#output results 
result = pd.read_sql(query, conn)
print("\nQuery Result:")
print(result)

#close connection
conn.close()
