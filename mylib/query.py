"""Query the database"""

import sqlite3


def query():
    """Query the database for the top 5 rows of the CarsDB table"""
    conn = sqlite3.connect("CarsDB.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM CarsDB LIMIT 5")
    print("Top 5 rows of the CarsDB table:")
    print(cursor.fetchall())
    conn.close()
    return "Success"



