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


def getting_possible_boards(board, n):
    """Function that return all possible
    boards 4x4 size"""
    boards = []
    for k in range(n - 3):
        for j in range(n - 3):
            possible_board = [i[j : 4 + j] for i in board[k : 4 + k]]
            boards.append(possible_board)
    return boards


def checking_function(horizontal_lines):
    result = None
    for i in horizontal_lines:
        if "-" in i:
            result = "unfinished!"
            continue
        elif i[0] == i[1] == i[2] == i[3]:
            return i[0] + " wins!"
        elif result is None:
            result = "draw!"
    return result


def tic_tac_toe_checker(board: List[List], n) -> str:
    possible_boards = getting_possible_boards(board, n)
    result = []
    for board in possible_boards:
        result.append(checking_function(board))

        vertical_lines = zip(board[0], board[1], board[2], board[3])
        result.append(checking_function(list(vertical_lines)))

        left_diagonal = [board[0][0], board[1][1], board[2][2], board[3][3]]
        right_diagonal = [board[0][3], board[1][2], board[2][1], board[3][0]]
        diagonals = [left_diagonal, right_diagonal]
        result.append(checking_function(diagonals))

    possible_results = ["x wins!", "o wins!", "unfinished!", "draw!"]

    for i in possible_results:
        if i in result:
            return i
