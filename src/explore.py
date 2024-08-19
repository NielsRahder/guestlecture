import pandas as pd
import os

# Define the path to the CSV file
csv_file_path = os.path.join('..', 'data', 'data.csv')

# Load the dataset from the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)

# Function to display the first few rows of the dataset or a specific column
def display_head(column_name=None):
    if column_name:
        if column_name in df.columns:
            print(f"\nFirst 5 Rows of the '{column_name}' Column:")
            print(df[[column_name]].head())
        else:
            print(f"Column '{column_name}' not found in the dataset.")
    else:
        print("\nFirst 5 Rows of the Dataset:")
        print(df.head())

# Function to display column names with their respective data types
def display_column_info():
    print("\nColumn Names and Data Types:")
    print(df.dtypes)

def display_summary_statistics(column_name = None):
        if column_name: 
            if column_name in df.columns:
                print(f"\nSummary Statistics for the '{column_name}' Column:")
                print(df[column_name].describe())
            else:
                print(f"Column '{column_name}' not found in the dataset.")
        else:
            print("\nSummary Statistics:")
            print(df.describe())


# Main exploration function
def explore_data():
    while True:
        print("\nData Exploration Options:")
        print("1. View the first 5 rows of the dataset or a specific column")
        print("2. View column names and their data types")
        print("3. View summary statistics")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            column_choice = input("Do you want to view a specific column? (y/n): ").strip().lower()
            if column_choice == 'y':
                column_name = input("Enter the column name: ")
                display_head(column_name)
            else:
                display_head()
        elif choice == '2':
            display_column_info()
        elif choice == '3':
            column_choice = input("Do you want to view summary statistics for a specific column? (y/n): ").strip().lower()
            if column_choice == 'y':
                column_name = input("Enter the column name: ")
                display_summary_statistics(column_name)
            else: 
                display_summary_statistics()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")

# Run the exploration
explore_data()
