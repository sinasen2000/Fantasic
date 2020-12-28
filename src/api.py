import logging
import os
import pprint
import warnings

import pytest
from dotenv import load_dotenv

import json
from datetime import date

import yfpy
from yfpy import Data
from yfpy.query import YahooFantasySportsQuery

# Suppress YahooFantasySportsQuery debug logging
logging.getLogger("yfpy.query").setLevel(level=logging.INFO)

# Ignore resource warnings from unittest module
warnings.simplefilter("ignore", ResourceWarning)

# load python-dotenv to parse environment variables
env_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".env")
load_dotenv(dotenv_path=env_path)

# Turn on/off example code stdout printing output
print_output = False

# Turn on/off automatic opening of browser window for OAuth
browser_callback = True

# Put private.json (see README.md) in test/ directory
auth_dir = "."

# Example code will output data here
data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test_output")



game_key = "402"
game_code = "nba"
season = "2021"
league_id = "39065"


yahoo_data = Data(data_dir)
yahoo_query = YahooFantasySportsQuery(
    auth_dir,
    league_id,
    game_id=game_key,
    game_code=game_code,
    offline=False,
    all_output_as_json=False,
    browser_callback=browser_callback
)

yahoo_query.league_key = game_key + ".l." + league_id
print(yahoo_query.get_team_roster_player_stats_by_week(1, 1))

def test_get_current_game_info():
    """Retrieve game info for current fantasy season.
    """
    query_result_data = yahoo_data.save("current-game-info", yahoo_query.get_current_game_info)
    print_output=True
    if print_output:
        pprint.pprint(query_result_data)
        print("-" * 100)
        print()
