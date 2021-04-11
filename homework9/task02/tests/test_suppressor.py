import pytest

from homework9.task02.task02 import Suppressor, suppressor


def test_zero_division_error_with_class():
    with Suppressor(ZeroDivisionError):
        10 / 0


def test_suppressing_possible_errors_with_generator():
    with suppressor(ZeroDivisionError):
        10 / 0


def test_that_zero_division_error_exception_raising():
    with pytest.raises(ZeroDivisionError):
        10 / 0


def test_type_error_with_class():
    with Suppressor(TypeError):
        2 + "3"


def test_type_error_with_generator():
    with suppressor(TypeError):
        2 + "3"


def test_that_type_error_exception_raising():
    with pytest.raises(TypeError):
        2 + "3"


def test_index_error_with_class():
    with Suppressor(IndexError):
        ["2 + 3"][2]


def test_index_error_with_generator():
    with suppressor(IndexError):
        ["2 + 3"][2]


def test_that_index_error_exception_raising():
    with pytest.raises(IndexError):
        ["2 + 3"][2]
