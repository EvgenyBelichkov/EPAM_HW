import pytest

from homework3.task04 import armstrong


@pytest.mark.parametrize(
    "number, expected_result",
    [
        [9, True],
        [10, False],
        [0, True],
        [54748, True],
        [200, False],
    ],
)
def test_of_armstrong_number(number, expected_result):
    assert armstrong.is_armstrong(number) == expected_result
