"""Query the database"""
import os
from databricks import sql
from dotenv import load_dotenv

# Global variable for the log file
LOG_PATH = "query_log.md"

def add_to_log(query_str, response="N/A"):
    """Append query and its result to a markdown log file"""
    with open(LOG_PATH, "a") as log_file:
        log_file.write(f"```sql\n{query_str}\n```\n\n")
        log_file.write(f"```Databricks response\n{response}\n```\n\n")

def query(query_str):
    """Execute a user-provided query"""

    load_dotenv()
    db_server = os.getenv("SERVER_HOSTNAME")
    token = os.getenv("ACCESS_TOKEN")
    api_path = os.getenv("HTTP_PATH")
    
    with sql.connect(
        server_hostname=db_server,
        http_path=api_path,
        access_token=token,
    ) as conn:
        cursor = conn.cursor()
        cursor.execute(query_str)
        result = cursor.fetchall()
    cursor.close()
    
    add_to_log(query_str, result)



