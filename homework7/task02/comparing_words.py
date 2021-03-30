"""
Given two strings. Return if they are equal when both are typed into
empty text editors. # means a backspace character.
Note that after backspacing an empty text, the text will continue empty.
Examples:
    Input: s = "ab#c", t = "ad#c"
    Output: True
    # Both s and t become "ac".
    Input: s = "a##c", t = "#a#c"
    Output: True
    Explanation: Both s and t become "c".
    Input: a = "a#c", t = "b"
    Output: False
    Explanation: s becomes "c" while t becomes "b".
"""


def checking_function(word: str):
    symbols = list()
    for i in word:
        if i == "#" and len(symbols) > 0:
            del symbols[-1]
        elif i != "#":
            symbols.append(i)
    return "".join(symbols)


def backspace_compare(first: str, second: str):
    return checking_function(first) == checking_function(second)
