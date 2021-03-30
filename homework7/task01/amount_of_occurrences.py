"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.
Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from typing import Any


def find_occurrences(tree: dict, element: Any) -> int:
    number_of_occurrences = 0
    if isinstance(tree, dict):
        tree = tree.values()
    for value in tree:
        if value == element:
            number_of_occurrences += 1
        if isinstance(value, (list, set, dict, tuple)):
            number_of_occurrences += find_occurrences(value, element)
    return number_of_occurrences
