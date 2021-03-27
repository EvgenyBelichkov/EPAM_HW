"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.
Write a function that accept any iterable of unique values and then
it behaves as range function:
import string
assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']
"""


def custom_range(sequence, start=None, finish=None, step=1):
    start_position = None
    finish_position = None
    symbols = []
    position = 0
    for i in sequence:
        if i == start:
            start_position = position
        if i == finish:
            finish_position = position
        symbols.append(i)
        position += 1
    symbols = symbols[start_position:finish_position:step]
    return symbols
