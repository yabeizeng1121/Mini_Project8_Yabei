"""
ETL-Query script
"""
import sys
import argparse
from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import query


def process_cli_args():
    """Manage command line inputs"""
    cli_parser = argparse.ArgumentParser(description="Enhanced ETL-Query tool")
    cli_parser.add_argument(
        "task",
        choices=["data_extraction", "data_loading", "data_query", "complete_etl"],
        help="Select the task to execute",
    )
    return cli_parser.parse_args()


def main():
    cli_args = process_cli_args()

    try:
        if cli_args.task == "data_extraction":
            print("Initiating data extraction...")
            data_file = extract()
            print(f"Extraction successful. Data saved at {data_file}\n")

        elif cli_args.task == "data_loading":
            print("Initiating data transformation and loading...")
            load("cars.csv")  # Assuming the file name is cars.csv
            print("Transformation and loading completed.\n")

        elif cli_args.task == "data_query":
            print("Initiating data querying...")
            query()
            print("Querying process completed.\n")

        elif cli_args.task == "complete_etl":
            print("Starting the full ETL process...")
            data_file = extract()
            print(f"Extraction successful. Data saved at {data_file}\n")
            load(data_file)
            print("Transformation and loading completed.\n")
            query()
            print("Querying process completed.\n")

    except Exception as err:
        print(f"An issue occurred: {err}", file=sys.stderr)


if __name__ == "__main__":
    main()
