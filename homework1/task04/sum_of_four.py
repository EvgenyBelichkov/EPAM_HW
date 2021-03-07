"""
Classic task, a kind of walnut for you
Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.
We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""

import itertools
from typing import List


def check_sum_of_four(
    a: List[int], b: List[int], c: List[int], d: List[int]
) -> int:  # code with separates lists on 2 parts
    result = 0
    sum_first_pairs = {}
    for i in a:
        for j in b:
            if i + j not in sum_first_pairs.keys():
                sum_first_pairs[i + j] = 1
            else:
                sum_first_pairs[i + j] += 1
    for k in c:
        for l in d:
            if (k + l) * (-1) in sum_first_pairs.keys():
                result += sum_first_pairs[(k + l) * (-1)]
    return result


def itertools_1(
    a: List[int], b: List[int], c: List[int], d: List[int]
) -> int:  # first code using itertools
    sum_itertools = {}
    result = 0
    for i in itertools.product(a, b):
        if i[0] + i[1] not in sum_itertools:
            sum_itertools[i[0] + i[1]] = 1
        else:
            sum_itertools[i[0] + i[1]] += 1
    for j in itertools.product(c, d):
        if (j[0] + j[1]) * (-1) in sum_itertools:
            result += sum_itertools[(j[0] + j[1]) * (-1)]
    return result


def itertools_2(
    a: List[int], b: List[int], c: List[int], d: List[int]
) -> int:  # second code using itertools
    result = 0
    for i in itertools.product(a, b, c, d):
        if i[0] + i[1] + i[2] + i[3] == 0:
            result += 1
    return result
