import os
from databricks import sql
import pandas as pd
from dotenv import load_dotenv

# Load the csv file and insert into databricks
def load(dataset="data/dem_candidates.csv", dataset2="data/rep_candidates.csv"):
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
        
        # Check if DemCandidatesDB table exists
        c.execute("SHOW TABLES FROM default LIKE 'dem_candidates*'")
        result = c.fetchall()
        if not result:
            c.execute(
                """
                CREATE TABLE IF NOT EXISTS DemCandidatesDB (
                    Name string,
                    Age int,
                    Occupation string,
                    State string,
                    Donations int
                )
                """
            )
            # Insert data into DemCandidatesDB
            for _, row in df.iterrows():
                convert = tuple(row)
                c.execute(f"INSERT INTO DemCandidatesDB VALUES {convert}")
        
        # Check if RepCandidatesDB table exists
        c.execute("SHOW TABLES FROM default LIKE 'rep_candidates*'")
        result = c.fetchall()
        if not result:
            c.execute(
                """
                CREATE TABLE IF NOT EXISTS RepCandidatesDB (
                    Name string,
                    Age int,
                    Occupation string,
                    State string,
                    Donations int
                )
                """
            )
            # Insert data into RepCandidatesDB
            for _, row in df2.iterrows():
                convert = tuple(row)
                c.execute(f"INSERT INTO RepCandidatesDB VALUES {convert}")
        
        c.close()

    return "success"

# load()
