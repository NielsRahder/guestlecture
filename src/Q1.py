import pandas as pd
import os
import sqlite3

# Define the path to the SQLite database
db_file_path = os.path.join('..', 'data', 'example.db')

# Connect to the SQLite database
conn = sqlite3.connect(db_file_path)

# Define the SQL query
query = """
SELECT 
DISTINCT MSRP
FROM cars
"""

# Execute the query and load the result into a pandas DataFrame
result = pd.read_sql(query, conn)

# Display the query result
print("\nQuery Result:")
print(result)

# Close the database connection
conn.close()
