### Q2 ###
###Find the total number of vehicles for each make that either (a) are eligible for the Clean Alternative Fuel Vehicle (CAFV) program and have an electric range of 300 miles or less, or (b) are not eligible for the CAFV program due to low battery range but have an electric range greater than 300 miles. 
###List the results grouped by vehicle make, and order them in descending order of the total vehicle count.
 
import pandas as pd
import os
import sqlite3

# Path to the SQLite database
db_file_path = os.path.join('data', 'example.db')
conn = sqlite3.connect(db_file_path)

# Your SQL query goes here
query = """
SELECT COUNT(*), Make
FROM cars
WHERE (CAFV_Eligibility = 'Clean Alternative Fuel Vehicle Eligible' AND EV_Range <= 300)
    OR (CAFV_Eligibility = 'Not eligible due to low battery range' AND EV_Range > 300)
    GROUP BY Make
    ORDER by COUNT(*) DESC
"""

#output results
result = pd.read_sql(query, conn)
print("\nQuery Result:")
print(result)

#close connection
conn.close()
