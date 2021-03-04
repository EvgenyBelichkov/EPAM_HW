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
    with open(file_name) as fi:
        lst = fi.readlines()
        elements = list()
        for index in range(len(lst)):
            el = int(lst[index].strip("\n"))
            elements.append(el)
    result = list()
    for i in elements:
        if len(result) == 0:
            result.append(i)
            result.append(i)
        if i < result[0]:
            result[0] = i
        if i > result[1]:
            result[1] = i
    maximum_and_minimum = (result[0], result[1])
    return maximum_and_minimum
