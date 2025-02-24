"""Testing file for extract.py"""

from unittest.mock import MagicMock


import pytest
import psycopg2
from psycopg2.extensions import connection
from extract import get_most_recent_brawler_data

def test_get_most_recent_brawler_data_returns_conection():
    """Tests get_most_recent_brawler_data returns connection"""

    conn = MagicMock()
    mock_fetch = conn.cursor().__enter__().fetchall
    mock_fetch.return_value = {"brawler_name": "mock_brawler_name"}
    result = get_most_recent_brawler_data(conn)

    assert result == {"brawler_name": "mock_brawler_name"}
