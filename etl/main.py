"""Main pipeline file to ru full etl on brawler data into the database"""

from os import environ

from dotenv import load_dotenv

from extract import extract_brawler_data_api, extract_brawler_data_database
from transform import transform_brawl_data_api

if __name__ =="__main__":

    load_dotenv()

    config = environ

    brawler_data_database = extract_brawler_data_database(config)

    brawler_data_api = extract_brawler_data_api(config)

    brawler_data_api = transform_brawl_data_api(brawler_data_api)
