### Q3 ###
## What is the most common Violation on locations that contain the word 'Road'? 

import pandas as pd
import os
import sqlite3

# Define the path to the SQLite database
db_file_path = os.path.join('data', 'example.db')

# Connect to the SQLite database
conn = sqlite3.connect(db_file_path)

# Your SQL query goes here
query = """
SELECT Violation, COUNT(*) as violation_count
FROM tickets
WHERE Location LIKE '%Road%'
GROUP BY Violation
ORDER BY violation_count DESC
"""

#output results 
result = pd.read_sql(query, conn)
print("\nQuery Result:")
print(result)

#close connection
conn.close()
