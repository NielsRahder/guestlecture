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
SELECT Make, Count(*) as count
FROM tickets
WHERE year = '2020' and month = '8'
GROUP BY Make
ORDER BY count DESC
LIMIT 1
"""

#output results 
result = pd.read_sql(query, conn)
print("\nQuery Result:")
print(result)

#close connection
conn.close()
