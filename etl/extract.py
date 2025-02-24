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


#TODO Finish function
def get_most_recent_brawler_data(conn: connection):
    """Returns most recent brawler data in database"""

    with conn.cursor() as cur:
        try:
            
            cur.execute("""SELECT b.brawler_id, brawler_version, brawler_name,
                        sp.starpower_id, sp.starpower_version, sp.starpower_name,
                        g.gadget_id, g.gadget_version, g.gadget_name,
                        FROM brawler b
                        INNER JOIN starpower sp ON 
                        (b.brawler_id = sp.brawler_id AND b.brawler_version = sp.brawler_version)
                        INNER JOIN gadget g ON 
                        (b.brawler_id = g.brawler_id AND b.brawler_version = g.brawler_version)
                        GROUP BY b.brawler_id, brawler_version, brawler_name,
                        sp.starpower_id, sp.starpower_version, sp.starpower_name,
                        g.gadget_id, g.gadget_version, g.gadget_name
                        """)
            
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
        