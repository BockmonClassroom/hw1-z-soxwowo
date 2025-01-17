# Jitong Zou
# January 17th, 2025

import csv
import pandas as pd

def read_with_csv(file_path):
    """
    Reads the CSV file using Python's built-in csv module and prints each row.

    Args:
        file_path (str): Path to the CSV file.
    """
    try:
        # Open the CSV file
        with open(file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)  
            
            # Loop through each row in the CSV
            for row in reader:
                print(row)  
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred while reading the file with csv: {e}")

def read_with_pandas(file_path):
    """
    Reads the CSV file using the pandas library and prints each row with its index.

    Args:
        file_path (str): Path to the CSV file.
    """
    try:
        # Load the CSV file into a pandas DataFrame
        data = pd.read_csv(file_path)

        # Loop through each row using pandas' itertuples method
        for row in data.itertuples(name="IrisRow"):
            print(f"Row #{row.Index}")  
            print(row)  
            print()  
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred while reading the file with pandas: {e}")

if __name__ == "__main__":
    # Define the path to the CSV file
    file_path = 'data/Iris.csv'

    print("Reading file using the csv module:\n")
    # Call the function using csv module
    read_with_csv(file_path)  

    print("\nReading file using the pandas library:\n")
    # Call the function using pandas
    read_with_pandas(file_path)  