import os
import pandas as pd
from databricks import sql
from dotenv import load_dotenv

def load_data(dataset_path="cars.csv"):
    """Load data into the Azure Databricks database"""
    
    # Read the CSV file into a pandas DataFrame
    data_frame = pd.read_csv(dataset_path, delimiter=",", skiprows=1)
    
    # Load environment variables
    load_dotenv()
    db_server = os.getenv("DB_SERVER")
    token = os.getenv("DB_TOKEN")
    api_path = os.getenv("DB_API_PATH")
    
    # Connect to Azure Databricks
    with sql.connect(
        server_hostname=db_server,
        http_path=api_path,
        access_token=token,
    ) as conn:
        cursor = conn.cursor()
        
        # Check if the table exists
        cursor.execute("SHOW TABLES FROM default LIKE 'CarsDB'")
        result = cursor.fetchall()
        
        # If the table doesn't exist, create it
        if not result:
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS CarsDB (
                    id int,
                    brand string,
                    model string,
                    year int,
                    price float
                )
                """
            )
            
            # Insert data into the table
            for _, row in data_frame.iterrows():
                values = (_,) + tuple(row)
                cursor.execute(f"INSERT INTO CarsDB VALUES {values}")
        
        cursor.close()

    return "Data loaded successfully"

