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
The `query.py` script provides functionalities to execute SQL queries on a Databricks database. It not only executes the queries but also maintains a log of the executed query and its result in a markdown file.

### Key Components

1. **Imported Libraries**:
    - `os`: Access environment variables.
    - `databricks`: Interface with Databricks using SQL.
    - `dotenv`: Load environment variables from a `.env` file.

2. **LOG_PATH**:
    A global variable specifying the path to the markdown log file where query logs will be maintained.

3. **`add_to_log(query_str, response="N/A")` Function**:
    - **Purpose**: Append a provided query and its corresponding response to the markdown log file.
    - **Parameters**:
        - `query_str`: The SQL query string that was executed.
        - `response`: The result of the query. By default, it's set to "N/A".
    - **Implementation**: The function writes the query and its response in separate code blocks in the markdown file, making it easy to review and understand.

4. **`query(query_str)` Function**:
    - **Purpose**: Execute a user-provided SQL query on the Databricks database.
    - **Parameters**:
        - `query_str`: The SQL query string to be executed.
    - **Implementation**:
        1. Load environment variables from a `.env` file.
        2. Establish a connection to the Databricks server using the loaded credentials.
        3. Execute the provided SQL query.
        4. Fetch and return the result of the query.
        5. Log the executed query and its result using the `add_to_log` function.
   
## Results Preview
![lib](https://github.com/nogibjj/mini_project6_yabei/assets/143656459/0e8483ee-d989-465f-ba6d-dd8ddc9ce4b4)
![test](https://github.com/nogibjj/mini_project6_yabei/assets/143656459/daa0fb1c-90f5-4855-af3c-35e829eecde0)


