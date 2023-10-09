"""
Transforms and Loads data into Azure Databricks
"""
import os
import pandas as pd
from databricks import sql
from dotenv import load_dotenv

def load(dataset="data/dem_candidates.csv", dataset2="data/rep_incumbents.csv"):
    """Transforms and Loads data into the local databricks database"""
    df = pd.read_csv(dataset, delimiter=",", skiprows=1)
    df2 = pd.read_csv(dataset2, delimiter=",", skiprows=1)
    
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
        
        # Create DemCandidatesDB table if not exists
        c.execute(
            """
            CREATE TABLE IF NOT EXISTS DemCandidatesDB (
                id int,
                name string,
                age int,
                occupation string,
                education string
            )
            """
        )
        
        # Insert data into DemCandidatesDB
        for _, row in df.iterrows():
            values = tuple(row)
            c.execute(f"INSERT INTO DemCandidatesDB VALUES {values}")
        
        # Create RepIncumbentsDB table if not exists
        c.execute(
            """
            CREATE TABLE IF NOT EXISTS RepIncumbentsDB (
                id int,
                name string,
                age int,
                occupation string,
                education string
            )
            """
        )
        
        # Insert data into RepIncumbentsDB
        for _, row in df2.iterrows():
            values = tuple(row)
            c.execute(f"INSERT INTO RepIncumbentsDB VALUES {values}")
        
        c.close()

    return "success"
