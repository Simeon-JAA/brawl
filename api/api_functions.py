"""Functions for the API!"""

from os import environ

import psycopg2
from psycopg2.extensions import connection
from psycopg2.extras import RealDictCursor


def get_db_connection(config_env) -> connection:
    """Establishes connection with the database"""

    try:
        db_connection = psycopg2.connect(dbname = config_env["dbname"],
                         user = config_env["user"],
                         password = config_env["password"],
                         host = config_env["host"],
                         port = config_env["port"]
        )
    except Exception as exc:
        raise psycopg2.DatabaseError("Error: Cannot establish connection to database!") from exc

    return db_connection


def get_most_recent_brawler_gadgets(db_connection: connection) -> dict:
    """Returns most recent brawler gadgets in database"""

    with db_connection.cursor(cursor_factory=RealDictCursor) as cur:
        try:
            cur.execute("""SELECT DISTINCT b.brawler_id, b.brawler_name,
                        g.gadget_id, g.gadget_version, g.gadget_name
                        FROM brawler b
                        INNER JOIN (SELECT b_2.brawler_id, MAX(b_2.brawler_version) AS brawler_version
                                    FROM brawler b_2
                                    GROUP BY b_2.brawler_id) b_max
                        ON b.brawler_id = b_max.brawler_id 
                        AND b.brawler_version = b_max.brawler_version
                        INNER JOIN gadget g ON b.brawler_id = g.brawler_id 
                        INNER JOIN (SELECT g_2.gadget_id, MAX(g_2.gadget_version) AS gadget_version
                                    FROM gadget g_2
                                    GROUP BY g_2.gadget_id) g_max
                        ON g.gadget_id = g_max.gadget_id
                        AND g.gadget_version = g_max.gadget_version
                        GROUP BY b.brawler_id, b.brawler_version, b.brawler_name,
                        g.gadget_id, g.gadget_version, g.gadget_name;""")

            most_recent_brawler_data = cur.fetchall()

        except Exception as exc:
            raise psycopg2.DatabaseError("Error: Unable to retrieve data from database!") from exc

    return most_recent_brawler_data


if __name__ =="__main__":

    pass