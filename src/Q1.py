### Q2 ###
#Return the top 5 car brands with the highest average Electric Range
import pandas as pd
import os
import sqlite3

#path to the SQLite database
db_file_path = os.path.join( 'data', 'example.db')
conn = sqlite3.connect(db_file_path)

# Your SQL query goes here
query = """
SELECT 
    Make AS Car_Brand,
    AVG(EV_Range) AS Average_Electric_Range
FROM cars
GROUP BY Car_Brand
ORDER BY AVG(EV_Range) DESC
LIMIT 5
"""

#output results 
result = pd.read_sql(query, conn)
print("\nQuery Result:")
print(result)

#close connection
conn.close()
