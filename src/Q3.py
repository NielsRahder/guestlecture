### Q3 ###
##On what Month in the year were the most tickets issued? And what was the total fine amount for that month?

import pandas as pd
import os
import sqlite3

# Path to the SQLite database
db_file_path = os.path.join('data', 'example.db')
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
