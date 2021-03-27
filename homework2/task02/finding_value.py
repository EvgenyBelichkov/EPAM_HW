"""
Given an array of  size n, find the most common and the least common elements.
The most common element is the element that appears more than n // 2 times.
The least common element is the element that appears fewer than other.
You may assume that the array is non-empty and the most common element
always exist in the array.
Example 1:
Input: [3,2,3]
Output: 3, 2
Example 2:
Input: [2,2,1,1,1,2,2]
Output: 2, 1
"""
from collections import defaultdict
from typing import List, Tuple


def major_and_minor_elem(inp: List):
    dict_of_elements = defaultdict(int)
    for i in inp:
        dict_of_elements[i] += 1
    n = len(inp)
    c_max = n // 2
    c_min = min(dict_of_elements.values())
    maximum = None
    minimum = None
    for key in dict_of_elements:
        if dict_of_elements[key] > c_max:
            maximum = key
        if dict_of_elements[key] == c_min:
            minimum = key
    result = (maximum, minimum)
    return result
