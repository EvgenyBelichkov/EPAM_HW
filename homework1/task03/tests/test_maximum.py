import os

import pytest

from homework1.task03.find_maximum_and_minimum import scan

print(os.path.dirname(__file__))


@pytest.mark.parametrize(
    "file_name, expected_result",
    [
        [os.path.join(os.path.dirname(__file__), "test1.txt"), (-5000, 12000)],
        [os.path.join(os.path.dirname(__file__), "test2.txt"), (1, 10)],
        [os.path.join(os.path.dirname(__file__), "test3.txt"), (-10000, 20000)],
        [os.path.join(os.path.dirname(__file__), "test4.txt"), (1, 15)],
    ],
)
def test_maximum_and_minimum(file_name, expected_result):
    assert scan(file_name) == expected_result
