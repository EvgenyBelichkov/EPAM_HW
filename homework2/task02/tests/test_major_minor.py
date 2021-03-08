from typing import List, Tuple

import pytest

from homework2.task02 import major_and_minor


@pytest.mark.parametrize(
    "inp, expected_result",
    [
        [[3, 2, 3], (3, 2)],
        [[2, 2, 1, 1, 1, 2, 2], (2, 1)],
    ],
)
def test_major_minor(inp, expected_result):
    assert major_and_minor.major_and_minor_elem(inp) == expected_result
