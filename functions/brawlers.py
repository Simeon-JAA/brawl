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


def get_all_brawler_data(api_header: dict) -> list[dict]:
    """returns all brawler data"""

    try:
        response = r.get(f"https://api.brawlstars.com/v1/brawlers", headers=api_header)
        response_data = response.json()
        all_brawler_data = response_data["items"]

    except:
       raise Exception("Error: Unable to return brawler data")

    return all_brawler_data


def all_brawler_names(all_brawler_data: list[dict]) -> list[str]:
    """Returns all brawler names"""

    return [brawler["name"].capitalize() for brawler in all_brawler_data]


def all_brawler_ids(all_brawler_data: list[dict]) -> list[int]:
    """Returns all brawler id's"""

    return [brawler["id"] for brawler in all_brawler_data]


def refine_brawler_data(brawler_data: dict) -> dict:
    """Returns refined brawler data for a specific brawler to be used in frontend"""

    if not isinstance(brawler_data, dict):
        raise Exception("Error: 'brawler data' parameter is not an object.")
  
    brawler_data_refined =  {}

    brawler_data_refined["id"] = brawler_data["id"]
    brawler_data_refined["name"] = brawler_data["name"].capitalize()
    brawler_data_refined["star_powers"] = [key["name"].capitalize() for key in brawler_data["starPowers"]]
    brawler_data_refined["gadgets"] = [key["name"].capitalize() for key in brawler_data["gadgets"]]

    return brawler_data_refined


if __name__ =="__main__":

    load_dotenv()

    config = environ

    token = config["api_token"]

    api_header = get_api_header(token)

    all_brawler_data = get_all_brawler_data(api_header)

    b = []

    for brawler in all_brawler_data:
        b.append(refine_brawler_data(brawler))




    