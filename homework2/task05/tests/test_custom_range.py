from string import ascii_lowercase

import pytest

from homework2.task05 import custom_range_function


@pytest.fixture
def fixture_example1():
    sequence = "123456789"
    start = "1"
    finish = "5"
    expected_result = ["1", "2", "3", "4"]
    yield sequence, start, finish, expected_result


def test_of_custom_sequence_example1(fixture_example1):
    sequence, start, finish, expected_result = fixture_example1
    assert (
        custom_range_function.custom_range(
            sequence, start=fixture_example1[1], finish=fixture_example1[2]
        )
        == expected_result
    )


@pytest.fixture
def fixture_example2():
    sequence = ascii_lowercase
    finish = "g"
    expected_result = ["a", "b", "c", "d", "e", "f"]
    yield sequence, finish, expected_result


def test_of_custom_sequence_example2(fixture_example2):
    sequence, finish, expected_result = fixture_example2
    assert (
        custom_range_function.custom_range(sequence, finish=fixture_example2[1])
        == expected_result
    )


@pytest.fixture
def fixture_example3():
    sequence = ascii_lowercase
    start = "z"
    finish = "w"
    step = -1
    expected_result = ["z", "y", "x"]
    yield sequence, start, finish, step, expected_result


def test_of_custom_sequence_example3(fixture_example3):
    sequence, start, finish, step, expected_result = fixture_example3
    assert (
        custom_range_function.custom_range(
            sequence,
            start=fixture_example3[1],
            finish=fixture_example3[2],
            step=fixture_example3[3],
        )
        == expected_result
    )
