from collections import namedtuple
from string import ascii_lowercase

import pytest

from homework2.task05 import custom_range_function

Testset = namedtuple("Testset", ["arguments", "expected_result"])

example_without_step_parameter = Testset(
    arguments=dict(
        sequence="123456789",
        start="1",
        finish="5",
    ),
    expected_result=["1", "2", "3", "4"],
)
example_only_finish_parameter = Testset(
    arguments=dict(sequence=ascii_lowercase, finish="g"),
    expected_result=["a", "b", "c", "d", "e", "f"],
)
example_full = Testset(
    arguments=dict(
        sequence=ascii_lowercase,
        start="z",
        finish="w",
        step=-1,
    ),
    expected_result=["z", "y", "x"],
)
all_examples_to_test = [
    example_full,
    example_without_step_parameter,
    example_only_finish_parameter,
]


@pytest.mark.parametrize("testset", all_examples_to_test)
def test_of_custom_sequence_example1(testset):
    assert (
        custom_range_function.custom_range(**testset.arguments)
        == testset.expected_result
    )
