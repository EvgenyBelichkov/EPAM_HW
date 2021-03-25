from typing import List

import pytest

from homework1.task05.maximal_subarray import find_maximal_subarray_sum


@pytest.mark.parametrize(
    "lst, k, expected_result",
    [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, 16),
        ([-5, -10, -6, -2, -1, -2, -10], 3, -1),
        ([-5, -1, 5, 7, 9, 11, -1, -10], 4, 32),
    ],
)
def test_maximum_subarray(lst, k, expected_result):
    assert find_maximal_subarray_sum(lst, k) == expected_result
