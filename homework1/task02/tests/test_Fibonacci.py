from collections.abc import Sequence

import pytest

from EPAM_HW.homework1.task02.Fibonacci_sequence import check_fibonacci


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ((13, 21, 34, 55), True),
        ((0, 1, 2), False),
        ([2584, 4181, 6765, 10946, 17711], True),
    ],
)
def test_fibonacci(value: Sequence, expected_result: bool):
    result = check_fibonacci(value)

    assert result == expected_result
