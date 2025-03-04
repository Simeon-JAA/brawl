"""Transform script to clean data received by brawl API"""

import re
import pandas as pd
from pandas import DataFrame

def brawler_name_value_to_title(brawler_data: dict) -> dict:
    """Apply title() to all values for the 'name' key"""

    if not isinstance(brawler_data, dict):
        raise TypeError("Error: Brawler data is an incorrect type!")

    brawler_data_keys = ("name", "id", "starPowers", "gadgets")

    for key in brawler_data.keys():
        if key not in brawler_data_keys:
            raise KeyError("Error: Missing key from brawler data!")

    brawler_data["name"] = brawler_data["name"].title()

    for star_power in brawler_data["starPowers"]:
        star_power["name"] = star_power["name"].title()

    for gadget in brawler_data["gadgets"]:
        gadget["name"] = gadget["name"].title()

    return brawler_data


def to_snake_case(text: str) -> str:
    """Formats keys to snake_case"""

    if not isinstance(text, str):
        raise TypeError("Error: Text should be a string!")

    text = text.replace(" ", "")
    text = re.sub(r'([a-z0-9\s]{1})([A-Z]{1})', r'\1_\2', text)

    if not text:
        raise ValueError("Error: Text cannot be blank!")

    return text.lower()


def transform_brawl_data_api(brawl_data_api: list[dict]) -> list[dict]:
    """Transform and clean API brawl data"""

    brawl_data_keys = ("starPowers", "name", "gadgets", "id")

    for index, brawler in enumerate(brawl_data_api):

        brawler = brawler_name_value_to_title(brawler)
        brawler = {to_snake_case(k): v for k, v in brawler.items() if k in brawl_data_keys}
        brawl_data_api[index] = brawler

    return brawl_data_api


def get_new_exploded_column_names(column_name: str) -> list[str]:
    """Returns new column names for exploded column name"""

    new_column_names = []
    column_extensions = ("id", "name")

    for extension in column_extensions:
        new_column_names.append(f"{column_name[:-1]}_{extension}")

    return new_column_names


def brawl_api_data_to_df(brawl_data_api, explode_column: str) -> DataFrame:
    """Returns brawl api data as a dataframe"""

    brawl_data_api_df = pd.DataFrame(data = brawl_data_api,
                                     columns = ["id", "name", explode_column])
    brawl_data_api_df_exploded = brawl_data_api_df.explode(column=explode_column)
    brawl_data_api_df_exploded[get_new_exploded_column_names(explode_column)] = brawl_data_api_df_exploded[explode_column].apply(lambda x: pd.Series(x))
    brawl_data_api_df_exploded = brawl_data_api_df_exploded.drop(columns = explode_column)
    brawl_data_api_df_exploded = brawl_data_api_df_exploded.reset_index(drop=True)

    return brawl_data_api_df_exploded


def filter_star_powers(brawler_data: dict) -> dict:
    """Returns data required for updating star power"""

    keys = ("id", "name", "star_powers")

    return {k: v for k, v in brawler_data.items() if k in keys}


def changes_to_star_power(star_power_data_database: DataFrame,
                          star_power_data_api: dict) -> bool:
    """Returns true if changes to a brawlers star power is detected"""

    for star_power in star_power_data_api["star_powers"]:

        star_power_id = star_power["id"]
        # print(star_power_id)
        # comparison_data = [k for k in star_power_data_database
                          #  if star_power_id in star_power_data_database]

        # print(comparison_data)

    print(pd.DataFrame(star_power_data_database))
    return


def get_starpower_changes(star_power_data_database: DataFrame, brawl_data_api: dict) -> dict:
    """Compares data between database and api and returns the difference to be inserted"""

    for brawler in brawl_data_api:

        brawler_star_power_df = star_power_data_database[
            star_power_data_database["brawler_id"] == brawler["id"]]

        if brawler["name"] == "Bull":
            star_power_data_api = filter_star_powers(brawler)
            changes_to_star_power(brawler_star_power_df, star_power_data_api)
    return


if __name__ =="__main__":

    pass
