"""Testing file for transform.py"""

import pytest


from transform import to_snake_case


def test_to_snake_case_base_case_1():
    """Tests base case for to_snake_case"""

    result = to_snake_case("camelCase")

    assert result == "camel_case"


def test_to_snake_case_base_case_2():
    """Tests base case for to_snake_case"""

    result = to_snake_case("camelCasecamelCase")

    assert result == "camel_casecamel_case"


def test_to_snake_case_base_case_3():
    """Tests base case for to_snake_case"""

    result = to_snake_case("snakecase")

    assert result == "snakecase"


def test_to_snake_case_base_case_4():
    """Tests base case for to_snake_case"""

    result = to_snake_case("snakeCase")

    assert result == "snake_case"


def test_to_snake_case_base_case_5():
    """Tests base case for to_snake_case"""

    result = to_snake_case("snake1Case")

    assert result == "snake1_case"


def test_to_snake_case_base_case_6():
    """Tests base case for to_snake_case"""

    result = to_snake_case("snake1 Case")

    assert result == "snake1_case"


def test_to_snake_case_base_case_7():
    """Tests base case for to_snake_case"""

    result = to_snake_case("UpperCamelCase")

    assert result == "upper_camel_case"


def test_to_snake_case_base_case_8():
    """Tests base case for to_snake_case"""

    result = to_snake_case("Upper Camel Case")

    assert result == "upper_camel_case"


def test_to_snake_case_edge_case_1():
    """Tests esge case for to_snake_case"""

    with pytest.raises(Exception):
        to_snake_case("")


def test_to_snake_case_edge_case_2():
    """Tests esge case for to_snake_case"""

    with pytest.raises(Exception):
        to_snake_case(" ")


def test_to_snake_case_edge_case_3():
    """Tests esge case for to_snake_case"""

    with pytest.raises(Exception):
        to_snake_case(1)
