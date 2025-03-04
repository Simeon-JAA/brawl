"""Load file for loading changes into database"""

from os import environ

import psycopg2
from psycopg2.extensions import connection
from dotenv import load_dotenv

def get_db_connection(config_env) -> connection:
    """Establishes connection with the database"""

    try:
        db_conn = psycopg2.connect(dbname = config_env["dbname"],
                         user = config_env["user"],
                         password = config_env["password"],
                         host = config_env["host"],
                         port = config_env["port"]
        )

    except Exception as exc:
        raise ConnectionError("Error: Cannot establish connection to database!") from exc

    return db_conn


def insert_new_brarler_data(db_conn: connection, brawler_data: dict):
    """Inserts new brawler data into the database"""

    if not isinstance(brawler_data, dict):
        raise TypeError("Error: Brawler data is not a dictionary!")

    if not brawler_data:
        raise ValueError("Error: Brawler data cannot be empty!")

    with db_conn.cursor() as cur:
        try:

            cur.execute("""""")

        except Exception as exc:
            raise ConnectionError("Error: Unable to insert data!") from exc



if __name__ =="__main__":

    load_dotenv()

    config = environ

    conn = get_db_connection(config)

    insert_new_brarler_data(conn, "temp")

    conn.close()
