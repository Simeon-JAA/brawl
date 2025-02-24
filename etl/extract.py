"""Extract file for  chages into database"""

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
        raise ConnectionError("Error: Cannot establish connection to database!")
    
    return conn


def get_most_recent_brawler_data(conn: connection):
    """Returns most recent brawler data in database"""

    with conn.cursor() as cur:
        try:
            
            cur.execute("""""")
            most_recent_brawler_data = cur.fetchall()

        except:
            raise ConnectionError("Error: Unable to retrieve data!")

    return most_recent_brawler_data


if __name__ =="__main__":
   
    load_dotenv()

    config = environ

    conn = get_db_connection(config)

    brawler_data = get_most_recent_brawler_data(conn)

    conn.close()
        