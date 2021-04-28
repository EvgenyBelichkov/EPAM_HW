from collections import namedtuple

import pytest

from homework7.task01.amount_of_occurrences import find_occurrences

dict1 = {"abc": ["a", "b", "c"], "def": ["d", "e", "c", {"efg": "c"}]}

dict2 = {
    1: [True, "b", "c"],
    2: ["d", "e", False, {"efg": "c", "4": [{"a": "a", "b": True}, True]}],
    3: True,
}

params = namedtuple("params", ["dict", "element", "expected_result"])

example = [
    params(dict=dict1, element="c", expected_result=3),
    params(dict=dict2, element=True, expected_result=4),
]


@pytest.mark.parametrize("data", example)
def test_find_occurrences_with_dict1(data):
    assert find_occurrences(data.dict, data.element) == data.expected_result
