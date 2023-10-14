## User Guide for ETL-Query Tool

### Introduction

The ETL-Query tool is designed to streamline the process of extracting, transforming, loading (ETL), and querying data. This guide provides step-by-step instructions on how to install and use the tool effectively.

### Installation

1. **Clone the Repository**:
   First, you need to clone the repository to your local machine:
git clone xxx
2. **Install the Package**:
Navigate to the directory containing `setup.py` and install the package using pip:
pip install .
### Usage

1. **Data Extraction**:
To extract data from the specified URL and save it to a local CSV file, use:
etl_query extract
2. **Data Transformation and Loading**:
To transform the dataset type and load it to Databricks, use:
etl_query transform_load
3. **Data Querying**:
To perform SQL queries on the loaded dataset, use:
etl_query general_query "YOUR SQL QUERY HERE"
### Database Communication

The tool is currently set up to communicate with a Databricks database. Ensure you have the necessary credentials and environment variables set up for successful communication.

### Troubleshooting

1. **Dependencies**:
Ensure all required Python libraries are installed. You can check the `requirements.txt` file for a list of necessary libraries.

2. **Database Connection**:
If you encounter issues connecting to the database, ensure your environment variables are correctly set up and that you have the necessary permissions to access the database.

3. **Data Format**:
Ensure the data you're working with matches the expected format detailed in the `README.md`.

### Feedback and Support

For any issues, feedback, or suggestions, please open an issue on the GitHub repository, and we'll address it promptly.
