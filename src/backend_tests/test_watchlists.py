import unittest
import os
from models.User import Users
from models.Watchlist import Watchlist
from models.Language import Languages
from main import create_app, db

class TestWatchlits(unittest.TestCase):
    #Runs before the tests
    @classmethod
    def test_get_all_watchlists(cls):
        pass