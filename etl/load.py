"""Load file for loading changes into database"""

from os import environ

import psycopg2
from psycopg2.extensions import connection
from dotenv import load_dotenv

def get_db_connection(config) -> connection:
    """Establishes connection with the database"""

    try:
        conn = psycopg2.connect(dbname = config["dbname"],
                         user = config["user"],
                         password = config["password"],
                         host = config["host"],
                         port = config["port"]
        )

    except:
        raise ConnectionError("Error: Cannot establish connection to database")
    
    return conn


def insert_new_brarler_data(conn: connection, brawler_data: dict):
    """Inserts new brawler data into the database"""

    with conn.cursor() as cur:
        try:
            
            cur.execute("""""")

        except:
            raise ConnectionError("Error: Unable to insert data")

    return


if __name__ =="__main__":
   
    load_dotenv()

    config = environ

    conn = get_db_connection(config)

    insert_new_brarler_data(conn, "temp")

    conn.close()
        