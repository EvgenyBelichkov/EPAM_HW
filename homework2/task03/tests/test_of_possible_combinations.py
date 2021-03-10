import pytest

from homework2.task03 import all_possible_lists


@pytest.fixture
def fixture():
    a = [[1, 2], [3, 4]]
    b = [[1, 3], [1, 4], [2, 3], [2, 4]]
    yield a, b


def test_function_that_returns_all_possible_lists1(fixture):
    a, b = fixture
    assert all_possible_lists.combinations(*a) == b


@pytest.fixture
def fixture():
    a = [[1, 1], [1, 1]]
    b = [[1, 1], [1, 1], [1, 1], [1, 1]]
    yield a, b


def test_function_that_returns_all_possible_lists2(fixture):
    a, b = fixture
    assert all_possible_lists.combinations(*a) == b
