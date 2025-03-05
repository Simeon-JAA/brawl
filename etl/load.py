"""Load file for loading changes into database"""

from os import environ

import psycopg2
from psycopg2.extensions import connection
from dotenv import load_dotenv

from extract import get_most_recent_brawler_version, get_most_recent_star_power_version

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


def insert_new_brawler_data(db_conn: connection, brawler_data: dict):
    """Inserts new brawler data into the database"""

    if not isinstance(brawler_data, dict):
        raise TypeError("Error: Brawler data is not a dictionary!")
    if not brawler_data:
        raise ValueError("Error: Brawler data cannot be empty!")
    
    try:
        brawler_version = get_most_recent_brawler_version(db_conn, brawler_data["id"])
    except Exception as exc:
        raise psycopg2.DatabaseError("Error: Unable to retrieve brawler version!") from exc

    with db_conn.cursor() as cur:
        try:
            cur.execute("""INSERT INTO brawler 
                        (brawler_id, brawler_version, brawler_name)
                        VALUES (%s, %s, %s);""", [brawler_data["id"], brawler_version, brawler_data["name"]])
        except Exception as exc:
            raise psycopg2.DatabaseError("Error: Unable to insert brawler data!") from exc


def insert_new_star_power_data(db_conn: connection, star_power_data: dict):
    """Inserts new starpower data into the database"""

    if not isinstance(star_power_data, dict):
        raise TypeError("Error: Starpower data is not a dictionary!")
    if not star_power_data:
        raise ValueError("Error: Starpower data cannot be empty!")
    
    try:
        starpower_version = get_most_recent_star_power_version(db_conn, star_power_data["id"])
    except Exception as exc:
        raise psycopg2.DatabaseError("Error: Unable to retrieve starpower version!") from exc

    with db_conn.cursor() as cur:
        try:
            cur.execute("""INSERT INTO starpower 
                        (starpower_id, starpower_version, starpower_name, brawler_id, brawler_version)
                        VALUES (%s, %s, %s, %s, %s);""", 
                        #TODO finish input arguments
                        [starpower_version])
        except Exception as exc:
            raise psycopg2.DatabaseError("Error: Unable to insert brawler data!") from exc



if __name__ =="__main__":

    load_dotenv()

    config = environ

    conn = get_db_connection(config)

    conn.close()
