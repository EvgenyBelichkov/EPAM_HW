from collections import namedtuple

import pytest

from homework2.task02 import finding_value

data = namedtuple("data", ["sequence", "expected_result"])
examples = [
    data([3, 2, 3], (3, 2)),
    data([2, 2, 1, 1, 1, 2, 2], (2, 1)),
    data([1, 2, 2, 3, 3, 4, 4, 4, 4, 4, 4], (4, 1)),
]


@pytest.mark.parametrize("input_sequence", examples)
def test_of_finding_major_and_minor_value_from_sequence(input_sequence):
    assert (
        finding_value.major_and_minor_elem(input_sequence.sequence)
        == input_sequence.expected_result
    )
