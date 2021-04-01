"""
Given a Tic-Tac-Toe 3x3 board (can be unfinished).
Write a function that checks if the are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"
Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished"
    [[-, -, o],
     [-, o, o],
     [x, x, x]]
     Return value should be "x wins!"
"""
from typing import List


def checking_function(horizontal_lines):
    result = None
    for i in horizontal_lines:
        if "-" in i:
            result = "unfinished!"
            continue
        elif i[0] == i[1] == i[2]:
            return i[0] + " wins!"
        elif result is None:
            result = "draw!"
    return result


def tic_tac_toe_checker(board: List[List]) -> str:
    result = [checking_function(board)]

    vertical_lines = zip(board[0], board[1], board[2])
    result.append(checking_function(list(vertical_lines)))

    left_diagonal = [board[0][0], board[1][1], board[2][2]]
    right_diagonal = [board[0][2], board[1][1], board[2][0]]
    diagonals = [left_diagonal, right_diagonal]
    result.append(checking_function(diagonals))

    possible_results = ["x wins!", "o wins!", "unfinished!", "draw!"]

    for i in possible_results:
        if i in result:
            return i
