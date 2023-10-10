
import csv
import os
from databricks import sql
from dotenv import load_dotenv

def load(dataset="data/performer-scores.csv", dataset2="data/show-data.csv"):
    
    with open(dataset, 'r') as file:
        reader = csv.reader(file)
        df = list(reader)

    with open(dataset2, 'r') as file:
        reader = csv.reader(file)
        df2 = list(reader)

    
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
        
        # Create performerscoresDB table if not exists
        c.execute(
            """
            CREATE TABLE IF NOT EXISTS performerscoresDB (
                Performer string,
                Score_per_year float,
                Total_score float,
                Show string
            )
            """
        )
        
        # Insert data into performerscoresDB
        for row in df[1:]:  # Skip the header row
            values = tuple(row)
            if not values or len(values) != 4:  
                print(f"Skipping invalid row: {row}")
                continue
            try:
                c.execute(f"INSERT INTO performerscoresDB VALUES {values}")
            except Exception as e:
                print(f"Error inserting row {row}: {e}")

        
        # Create showdataDB table if not exists
        c.execute(
            """
            CREATE TABLE IF NOT EXISTS showdataDB (
                Performer string,
                Show string,
                Show_Start string,
                Show_End string,
                CharEnd string
            )
            """
        )
        
        # Insert data into showdataDB
        for row in df2[1:]:  # Skip the header row
            values = tuple(row)
            if not values or len(values) != 5:  
                print(f"Skipping invalid row: {row}")
                continue
            try:
                c.execute(f"INSERT INTO showdataDB VALUES {values}")
            except Exception as e:
                print(f"Error inserting row {row}: {e}")

    
    return "success"

