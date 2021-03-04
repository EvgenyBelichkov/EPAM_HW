import pytest

from homework1.task04 import sum_of_four


@pytest.mark.parametrize(
    "lst1, lst2, lst3, lst4, result",
    [
        ([1, 2], [-2, 3], [4, 6], [0, -5], 1),
        ([1, 2, 3, 4], [-4, -3, -2, -1], [1, 2, 3, 4], [-4, -3, -2, -1], 44),
        (
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            4096,
        ),
    ],
)
def test_sum(lst1, lst2, lst3, lst4, result):
    assert sum_of_four.check_sum_of_four(lst1, lst2, lst3, lst4) == result
