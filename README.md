[![CI](https://github.com/nogibjj/Mini_Project5_Yabei_New/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Mini_Project5_Yabei_New/actions/workflows/cicd.yml)
# Mini Project 6
The ETL-Query tool is designed to streamline the process of extracting, transforming, loading (ETL) and querying data. It specifically caters to handling the 'cars' dataset. The tool offers flexibility by allowing users to either execute each phase of the ETL process independently or execute the complete ETL process in a single command.

## Requirements
1. Design a complex SQL query involving joins, aggregation, and sorting.
2. Provide an explanation for what the query is doing and the expected results.


## Preparation
1. Clone the GitHub repository.
2. Ensure that you have the necessary Python libraries installed.
3. Familiarize yourself with the four main files:
    - `__init__.py`: Module initialization file.
    - `extract.py`: Contains functions to extract data from the given URL.
    - `transform_load.py`: Houses functions to transform the dataset type and load it to Databricks.
    - `query.py`: Used to request and perform SQL queries on the dataset.

## Check Format
The tool expects the dataset in the following format:
- Filename: `cars.csv`
- Data columns and structure to be confirmed (based on your dataset's structure).

## Steps Guide
1. **Data Extraction**
    ```bash
    make extract
    ```
    This command extracts data from the specified URL and saves it to a local CSV file.

2. **Data Transformation and Loading**
    ```bash
    make transform_load
    ```
    This command transforms the dataset type and loads it to Databricks.

3. **Data Querying**
    ```bash
    make query
    ```
    Use this command to perform SQL queries on the loaded dataset.
    This command performs all the above steps in sequence: it extracts the data, loads it to Databricks, and then queries it.

## Results Preview


