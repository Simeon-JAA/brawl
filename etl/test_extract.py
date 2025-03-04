"""Testing file for extract.py"""

from unittest.mock import MagicMock


import pytest
from psycopg2.extensions import connection
from extract import get_most_recent_brawler_data

def test_get_most_recent_brawler_data_calls_excecute():
    """Tests get_most_recent_brawler_data calls the execute function"""

    conn = MagicMock()
    mock_fetch = conn.cursor().__enter__().fetchall
    get_most_recent_brawler_data(conn)

    assert mock_fetch.call_count == 1
