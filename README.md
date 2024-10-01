# Guestlecture for TiU

Students in the guestlecture are expected to first download the data via the `download.py` file after which the data can be explored via the `explore.py` file. 

Before you start, make sure you have the right requirements installed:

_Best practice is to do this in virtual enviroment_
`pip install -r requirements.txt`

To access the data, use these commands:
Car data = `select * from cars`
Ticket data = `select * from tickets`

Subsequently the following questions can be answered: 

- *Q1* Return the top 5 car brands with the highest average Electric Range
- *Q2* Find the total number of vehicles for each make that either (a) qualify for the Clean Alternative Fuel Vehicle (CAFV) program with an electric range of 300 miles or less, or (b) don't qualify for the CAFV program but have an electric range of more than 300 miles. List the results grouped by make, ordered by the total vehicle count in descending order.
- *Q3* On what Month in the year where the most tickets issued? And what was the total fine amount for that month?
- *Q4* What is the most common Violation on locations that contain the word 'Road'?
- *Q5* Which car brand has the most amount of tickets in August 2020?
- *Q6* Provide a list of all electric vehicle models offered by each car brand
