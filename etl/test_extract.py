"""Testing file for extract.py"""

from unittest.mock import MagicMock


import pytest
from extract import get_most_recent_brawler_data, get_most_recent_brawler_version

def test_get_most_recent_brawler_data_calls_excecute():
    """Tests get_most_recent_brawler_data calls the execute function"""

    conn = MagicMock()
    mock_fetch = conn.cursor().__enter__().fetchall
    get_most_recent_brawler_data(conn)

    assert mock_fetch.call_count == 1


def test_get_most_recent_brawler_version_edge_case_1():
    """Tests exception raised for wrong input type get_most_recent_brawler_version"""

    conn = MagicMock()
    with pytest.raises(TypeError):
        get_most_recent_brawler_version(conn, "this is not a brawler_id")


def test_get_most_recent_brawler_version_calls_execute():
    """Tests execute is called by cursor for get_most_recent_brawler_version"""

    conn = MagicMock()
    mock_execute = conn.cursor().__enter__().execute
    get_most_recent_brawler_version(conn, 1)

    assert mock_execute.call_count == 1


def test_get_most_recent_brawler_version_calls_fetchall():
    """Tests execute is called by cursor for get_most_recent_brawler_version"""

    conn = MagicMock()
    mock_fetch = conn.cursor().__enter__().fetchall
    get_most_recent_brawler_version(conn, 1)

    assert mock_fetch.call_count == 1
