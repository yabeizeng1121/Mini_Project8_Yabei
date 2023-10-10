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
# SQL Query Explanation

This SQL query is designed to extract specific information regarding performances from a database called `showdataDB`.

```sql
SELECT Performer, Show, 
        MIN(Show_Start) AS Earliest_Show_Start,
        MAX(Show_End) AS Latest_Show_End
        FROM showdataDB
        GROUP BY Performer, Show
        ORDER BY Earliest_Show_Start DESC
        LIMIT 10;
```


This query is pulling data from the `showdataDB` table, grouping it by the `Performer` and `Show` columns, calculating the earliest start time and latest end time for each group, sorting these groups by the earliest start time in descending order, and then limiting the result to the first 10 rows of this sorted list. This way, we get a compact list of performer-show pairs along with the range of show times, with the pairs having the latest start times listed first.



## Results Preview
![lib](https://github.com/nogibjj/mini_project6_yabei/assets/143656459/0e8483ee-d989-465f-ba6d-dd8ddc9ce4b4)
![test](https://github.com/nogibjj/mini_project6_yabei/assets/143656459/daa0fb1c-90f5-4855-af3c-35e829eecde0)


