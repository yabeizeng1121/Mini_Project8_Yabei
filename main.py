"""
ETL-Query script
"""
import sys
from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import query

def main():
    try:
        # Extract
        print("Extracting data...")
        file_path = extract() 
        print(f"Data extraction completed successfully. Saved to {file_path}\n")

        # Transform and Load
        print("Transforming and loading data...")                         
        load(file_path)                
        print("Data transformation and loading completed successfully.\n")

        # Query
        print("Querying data...")
        query()
        print("Data querying completed successfully.\n")

    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
