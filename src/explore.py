import pandas as pd
import os

# Define the paths to the CSV files
cars_file_path = os.path.join('data', 'cars_data.csv')
ticket_file_path = os.path.join('data', 'ticket_data.csv')

# Function to load the selected dataset
def load_dataset(dataset_choice):
    if dataset_choice == '1':
        print("Loading Cars dataset...")
        return pd.read_csv(cars_file_path)
    elif dataset_choice == '2':
        print("Loading Ticket dataset...")
        return pd.read_csv(ticket_file_path)
    else:
        print("Invalid choice. Loading Cars dataset by default.")
        return pd.read_csv(cars_file_path)

# Function to display the first few rows of the dataset or a specific column
def display_head(df, column_name=None):
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
def display_column_info(df):
    print("\nColumn Names and Data Types:")
    print(df.dtypes)

# Function to display summary statistics for the dataset or a specific column
def display_summary_statistics(df, column_name=None):
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
def explore_data(df):
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
                display_head(df, column_name)
            else:
                display_head(df)
        elif choice == '2':
            display_column_info(df)
        elif choice == '3':
            column_choice = input("Do you want to view summary statistics for a specific column? (y/n): ").strip().lower()
            if column_choice == 'y':
                column_name = input("Enter the column name: ")
                display_summary_statistics(df, column_name)
            else:
                display_summary_statistics(df)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")

# Main program loop for dataset selection
def main():
    print("Select a dataset to explore:")
    print("1. Cars dataset")
    print("2. Ticket dataset")
    
    dataset_choice = input("Enter your choice (1/2): ")

    df = load_dataset(dataset_choice)

    explore_data(df)


main()
