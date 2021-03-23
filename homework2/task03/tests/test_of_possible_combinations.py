from collections import namedtuple

import pytest

from homework2.task03 import all_possible_lists

data = namedtuple("data", ["a", "b"])
examples = [
    data(a=[[1, 2], [3, 4]], b=[[1, 3], [1, 4], [2, 3], [2, 4]]),
    data(a=[[1, 1], [1, 1]], b=[[1, 1], [1, 1], [1, 1], [1, 1]]),
    data(a=[[1, 2], [3], [4, 5]], b=[[1, 3, 4], [1, 3, 5], [2, 3, 4], [2, 3, 5]]),
]


@pytest.mark.parametrize("params", examples)
def test_function_that_returns_all_possible_lists(params):
    assert all_possible_lists.combinations(*params.a) == params.b
