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

from itertools import zip_longest


#
def checking_function(word: str):
    symbols = list()
    for i in word:
        if i == "#" and len(symbols) > 0:
            symbols.pop()
        elif i != "#":
            symbols.append(i)
    return "".join(symbols)


def backspace_compare_version1(first: str, second: str):
    return checking_function(first) == checking_function(second)


def returning_char(word):
    skip = 0
    for i in word[::-1]:
        if i == "#":
            skip += 1
        elif i != "#" and skip > 0:
            skip -= 1
        else:
            current_value = i
            yield current_value


def backspace_compare_version2(first: str, second: str):
    gen1 = returning_char(first)
    gen2 = returning_char(second)
    for _ in range(max(len(first), len(second))):
        try:
            if next(gen1) != next(gen2):
                return False
        except StopIteration:
            return True


def backspace_compare_version3(first: str, second: str):
    gen1 = returning_char(first)
    gen2 = returning_char(second)
    for i in list(zip_longest(gen1, gen2)):
        if i[0] != i[1]:
            return False
    return True
