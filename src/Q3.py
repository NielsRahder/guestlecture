### Q3 ###
## On what Month in the year where the most tickets issued? And what was the total fine amount for that month?

import pandas as pd
import os
import sqlite3

#path to the SQLite database
db_file_path = os.path.join('data', 'example.db')
conn = sqlite3.connect(db_file_path)

# Your SQL query goes here
query = """
SELECT Month, SUM(fine) as total_fine
FROM tickets
GROUP BY Month
ORDER BY total_fine DESC
LIMIT 1
"""

#output results
result = pd.read_sql(query, conn)
print("\nQuery Result:")
print(result)

#close connection
conn.close()
