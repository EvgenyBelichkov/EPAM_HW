import os

import pytest

from homework9.task01.task01 import merge_sorted_files


@pytest.fixture()
def data_files():
    return [
        os.path.join(os.path.dirname(__file__), "file1.txt"),
        os.path.join(os.path.dirname(__file__), "file2.txt"),
        os.path.join(os.path.dirname(__file__), "file3.txt"),
    ]


def test_correct_sequence(data_files):
    assert list(merge_sorted_files([data_files[0], data_files[1]])) == [
        1,
        2,
        3,
        4,
        5,
        6,
    ]
    assert list(merge_sorted_files([*data_files])) == [1, 2, 2, 3, 4, 5, 6, 10, 15]


def test_result_is_iterator(data_files):
    iterator = merge_sorted_files(list(data_files))
    next(iterator)
    next(iterator)
    next(iterator)
    assert list(iterator) == [3, 4, 5, 6, 10, 15]


def test_stop_iteration_error(data_files):
    iterator = merge_sorted_files([data_files[0], data_files[1]])
    for i in range(6):
        next(iterator)
    with pytest.raises(StopIteration):
        next(iterator)
