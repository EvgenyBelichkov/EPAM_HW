from collections import namedtuple

import pytest

from homework7.task03.tic_tac_toe import tic_tac_toe_checker

board = namedtuple("board", ["sequence", "expected_result", "n"])

data = [
    board(
        sequence=[
            ["-", "-", "o", "x", "o"],
            ["-", "x", "o", "o", "x"],
            ["x", " o", "x", "x", "o"],
            ["-", "x", "o", "o", "x"],
            ["x", " o", "x", "x", "o"],
        ],
        expected_result="unfinished!",
        n=5,
    ),
    board(
        sequence=[
            ["x", "o", "o", "x", "o"],
            ["x", "x", "o", "o", "x"],
            ["x", "o", "x", "x", "o"],
            ["x", "x", "o", "o", "x"],
            ["o", "o", "x", "x", "o"],
        ],
        expected_result="x wins!",
        n=5,
    ),
    board(
        sequence=[
            ["x", "o", "o", "x", "o"],
            ["o", "x", "o", "o", "o"],
            ["x", "o", "x", "o", "o"],
            ["x", "x", "o", "o", "x"],
            ["o", "o", "x", "x", "o"],
        ],
        expected_result="o wins!",
        n=5,
    ),
    board(
        sequence=[
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "o", "o", "o"],
            ["-", "-", "-", "-", "-", "-", "x", "x", "x", "x"],
        ],
        expected_result="x wins!",
        n=10,
    ),
]


@pytest.mark.parametrize("examples", data)
def test_tic_tac_toe_function(examples):
    assert (
        tic_tac_toe_checker(examples.sequence, examples.n) == examples.expected_result
    )
