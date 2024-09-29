### Q6 ###
## Provide a list of all electric vehicle models offered by each car brand
## Aggregate the results to avoid duplicating the 'Make' column.

import pandas as pd
import os
import sqlite3

# Define the path to the SQLite database
db_file_path = os.path.join('data', 'example.db')

# Connect to the SQLite database
conn = sqlite3.connect(db_file_path)

# Your SQL query goes here
query = """
SELECT Make, GROUP_CONCAT(DISTINCT Model ORDER BY Model ASC) AS Models
FROM cars
GROUP BY Make
ORDER BY Make ASC
"""

#output results 
result = pd.read_sql(query, conn)
print("\nQuery Result:")
print(result)

#close connection
conn.close()
