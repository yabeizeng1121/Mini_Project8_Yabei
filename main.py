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
        source_url = input("Enter the source URL: ") or None
                           
        extract(url=source_url)
        print("Data extraction completed successfully.\n")

        # Transform and Load
        print("Transforming and loading data...")
                           
        dataset_path = input("Enter the dataset path: ") or None
                           
        load(dataset=dataset_path)                 
        print("Data transformation and loading completed successfully.\n")

        # Query
        print("Querying data...")
        query()
        print("Data querying completed successfully.\n")

    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
