import logging
import os
import pprint
import warnings

import pytest
from dotenv import load_dotenv

from yfpy import Data
from yfpy.models import Game, StatCategories, User, Scoreboard, Settings, Standings, League, Player, Team, \
    TeamPoints, TeamStandings, Roster
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



game_key = "390"
game_code = "nba"
season = "2020"
league_id = "39065"

