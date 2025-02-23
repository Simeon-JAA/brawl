"""Scripts that return player data"""

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


def format_player_tag(player_tag: str) -> str:
    """Formats player tag"""

    if not isinstance(player_tag, str):
        raise Exception("Error: Player tag must be a string format!")
    
    player_tag = player_tag.strip().replace("#", "").upper()

    if not player_tag:
        raise Exception("Error: Player tag must not be empty!")
    
    return player_tag


def check_player_tag(player_tag: str) -> bool:
    """Returns true if player tage is accepted"""
    
    player_tag = format_player_tag(player_tag)

    if len(player_tag) < 3:
        return False
    
    allowed_characters = ['P', 'Y', 'L', 'Q', 'G', 'O', 'R', 'J', 'C', 'U', 'V', '0', '2', '8', '9']
    
    for character in player_tag:
        if character not in allowed_characters:
            return False
        
    return True


def get_player_data(api_header: dict, player_tag: str) -> dict:
    """Returns player data"""
    
    player_tag = format_player_tag(player_tag)

    if check_player_tag(player_tag):
        
      try:
          response = r.get(f"https://api.brawlstars.com/v1/players/%23{player_tag}", headers=api_header)
          response_data = response.json()
      
      except:
          raise Exception("Error: Unable to retrieve player data.")
    
      return response_data
    
    else:
        raise Exception("Error: Invalid player tag.")


#TODO get club data
#TODO format keys to snake case
def refine_player_stats(player_data: dict) -> dict:
    """Refined player data and returns chosen stats"""

    player_stats_keys = ["name", "trophies", "highestTrophies", "expLevel", "3vs3Victories",
                         "soloVictories", "duoVictories", "club"]
    
    player_stats = {k: v for k, v in player_data if k in player_stats_keys}

    return player_stats


#TODO format keys to snake case
def refine_player_brawlers(player_data: dict) -> list[dict]:
    """Refines player data on brawler's and return a list of all brawlers"""

    player_brawler_data = player_data["brawlers"]

    player_brawlers = []

    brawler_keys = ["name", "power", "rank", "trophies", "starPowers", "gadgets", "gears"]
      

    for item in player_brawler_data:
          brawler_data = {k: v for k, v in item.items() if k in brawler_keys}
          player_brawlers.append(brawler_data)

    return player_brawlers


if __name__ =="__main__":

    load_dotenv()

    config = environ

    token = config["api_token"]

    api_header = get_api_header(token)

    #Curently using my playerID
    player_data = get_player_data(api_header, "8QC8RP02")
    print(player_data)
    # print(refine_player_brawlers(player_data))