"""main.py for api"""

import os

from flask import Flask
from dotenv import load_dotenv

from api_functions import get_db_connection


app = Flask(__name__)    
@app.route('/brawlers', methods=['GET'])
def get_brawlers() -> dict:
    """Returns brawler data from database"""

    return 

if __name__ =="__main__":

    load_dotenv()

    config = os.environ

    app.run(debug=True, port=config["api_port"], load_dotenv=True)
