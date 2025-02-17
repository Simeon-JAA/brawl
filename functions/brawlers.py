"""Scripts that return info for all brawlers"""

import requests as r
from os import environ

from dotenv import load_dotenv


def get_api_header(token: str) -> dict:
   """Returns api header data"""

   header = {
      "Accept": "application/json",
      "Authorization": f"Bearer {token}"
   }

   return header


def get_all_brawler_data(header_data: dict) -> list[dict]:
    """returns all brawler data"""

    try:
        response = r.get(f"https://api.brawlstars.com/v1/brawlers", headers=header_data)
        response = response.json()
        all_brawler_data = response["items"]

    except:
       raise Exception("Error: Unable to return brawler data")

    return all_brawler_data


def all_brawler_names(all_brawler_data: list[dict]) -> list[str]:
    """Returns all brawler names"""

    return [brawler["name"].capitalize() for brawler in all_brawler_data]


def all_brawler_ids(all_brawler_data: list[dict]) -> list[int]:
    """Returns all brawler id's"""

    return [brawler["id"] for brawler in all_brawler_data]

#TODO Finish function
def refined_brawler_data(brawler_id: int, header_data: dict) -> dict:
    """Returns refined brawler data for a specific brawler to be used in frontend"""

    if not isinstance(brawler_id, int):
        raise Exception("Error: 'brawler_id' parameter is not integer.")
    
    brawler_data = {}

    try:
        response = r.get(f"https://api.brawlstars.com/v1/{brawler_id}/definitions/", headers=header_data)
        print(response.status_code)
        data = response.json()

    except:
        raise Exception("Error: Unable to retrieve brawler info.")
    
    return brawler_data


if __name__ =="__main__":

    load_dotenv()

    config = environ

    token = config["api_token"]

    api_header = get_api_header(token)

    all_brawler_data = get_all_brawler_data(api_header)

    print(all_brawler_data[0])


    