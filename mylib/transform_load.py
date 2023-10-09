
import csv
import os
from databricks import sql
from dotenv import load_dotenv

def load(dataset="data/performer-scores.csv", dataset2="data/show-data.csv"):
    # 使用csv模块读取CSV文件
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
        
        # Create DemCandidatesDB table if not exists
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
        
        # Insert data into DemCandidatesDB
        for _, row in df.iterrows():
            values = tuple(row)
            c.execute(f"INSERT INTO performerscoresDB VALUES {values}")
        
        # Create RepIncumbentsDB table if not exists
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
        
        # Insert data into RepIncumbentsDB
        for _, row in df2.iterrows():
            values = tuple(row)
            c.execute(f"INSERT INTO showdataDB VALUES {values}")
        
        c.close()

    return "success"
