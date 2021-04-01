from collections import namedtuple

import pytest

from homework7.task03.tic_tac_toe import tic_tac_toe_checker

board = namedtuple("board", ["sequence", "expected_result"])

data = [
    board(
        sequence=[["-", "-", "o"], ["-", "x", "o"], ["x", " o", "x"]],
        expected_result="unfinished!",
    ),
    board(
        sequence=[["-", "-", "o"], ["-", "o", "o"], ["x", "x", "x"]],
        expected_result="x wins!",
    ),
    board(
        sequence=[["o", "-", "-"], ["x", "o", "-"], ["x", " -", "o"]],
        expected_result="o wins!",
    ),
    board(
        sequence=[["x", "o", "o"], ["o", "x", "x"], ["x", " x", "o"]],
        expected_result="draw!",
    ),
    board(
        sequence=[["-", "-", "-"], ["-", "-", "-"], ["-", " -", "-"]],
        expected_result="unfinished!",
    ),
]


@pytest.mark.parametrize("examples", data)
def test_tic_tac_toe_function(examples):
    assert tic_tac_toe_checker(examples.sequence) == examples.expected_result
