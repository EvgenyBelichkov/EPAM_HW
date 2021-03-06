"""
Write down the function, which reads input line-by-line, and find maximum and minimum values.
Function should return a tuple with the max and min values.
For example for [1, 2, 3, 4, 5], function should return [1, 5]
We guarantee, that file exists and contains line-delimited integers.
To read file line-by-line you can use this snippet:
with open("some_file.txt") as fi:
    for line in fi:
        ...
"""
from typing import Tuple


def scan(file_name: str) -> Tuple[int, int]:
    minimum = None
    maximum = None
    with open(file_name) as fi:
        for line in fi:
            el = int(line.strip("\n"))
            if minimum is None:
                minimum = el
            if maximum is None:
                maximum = el
            if el < minimum:
                minimum = el
            if el > maximum:
                maximum = el
    maximum_and_minimum = (minimum, maximum)
    return maximum_and_minimum
