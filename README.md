[![CI](https://github.com/nogibjj/Mini_Project5_Yabei_New/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Mini_Project5_Yabei_New/actions/workflows/cicd.yml)
# Mini Project 6
The ETL-Query tool is designed to streamline the process of extracting, transforming, loading (ETL) and querying data. It specifically caters to handling the 'show_data' dataset and 'performer_score' dataset. The tool offers flexibility by allowing users to either execute each phase of the ETL process independently or execute the complete ETL process in a single command.

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
- Filename: `show_data.csv`, `performer_score.csv`

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

## Explanation of Query
In order to document and explain the Python script provided, which interfaces with a Databricks SQL database, you can create a Markdown file with the following content:

---

#### Query Script Documentation
Import Statements:
```python
import os
from databricks import sql
from dotenv import load_dotenv
```
Here, the script imports the necessary libraries:
- `os`: This module provides a way of using operating system dependent functionality like reading or writing to the file system.
- `databricks`: This library provides the SQL interface to Databricks.
- `dotenv`: This module allows you to specify environment variables in a `.env` file, which can then be loaded and accessed within your script.

#### Global Variable:
```python
LOG_FILE = "query_log.md"
```
A global variable `LOG_FILE` is defined to specify the name of the Markdown file where queries and their responses will be logged.

#### log_query Function:
```python
def log_query(query, result="none"):
    """adds to a query markdown file"""
    with open(LOG_FILE, "a") as file:
        file.write(f"```sql\n{query}\n```\n\n")
        file.write(f"```response from databricks\n{result}\n```\n\n")
```
The `log_query` function takes a SQL `query` and its `result` as arguments. It opens the log file in append mode and writes the query and result to it in a formatted manner.

#### general_query Function:
```python
def general_query(query):
    """runs a query a user inputs"""

    load_dotenv()
    server_h = os.getenv("SERVER_HOSTNAME")
    access_token = os.getenv("ACCESS_TOKEN")
    http_path = os.getenv("HTTP_PATH")
    with sql.connect(
        server_hostname=server_h,
        http_path=http_path,
        access_token=access_token,
    ) as connection:
        c = connection.cursor()
        c.execute(query)
        result = c.fetchall()
    c.close()
    log_query(f"{query}", result)
```
The `general_query` function is where the actual interaction with the Databricks database occurs. It first loads environment variables from a `.env` file using `load_dotenv`, then establishes a connection to the Databricks server using the `sql.connect` method. A cursor object is created with `connection.cursor()`, which is then used to execute the given `query` and fetch all results with `c.fetchall()`. Finally, the `log_query` function is called to log the query and its result to the log file.

#### Usage:
To utilize this script, you simply need to call the `general_query` function with your SQL query as an argument:

## Results Preview
![lib](https://github.com/nogibjj/mini_project6_yabei/assets/143656459/0e8483ee-d989-465f-ba6d-dd8ddc9ce4b4)
![test](https://github.com/nogibjj/mini_project6_yabei/assets/143656459/daa0fb1c-90f5-4855-af3c-35e829eecde0)


