import pytest


@pytest.fixture
def file_names():
    return ["tests_data/test_table.csv"]


@pytest.fixture
def rate():
    return [("apple", 4.9), ("samsung", 4.8)]


@pytest.fixture
def price():
    return [("samsung", 1199.0), ("apple", 999.0)]
