"""
Given a list of integers numbers "nums".
You need to find a sub-array with length less equal to "k", with maximal sum.
The written function should return the sum of this sub-array.
Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    sum_list = []
    for i in range(len(nums)):
        s = nums[i]
        if i < len(nums) - k:
            for j in range(1, k):
                if s + nums[i + j] > s:
                    s = s + nums[i + j]
        else:
            for j in range(1, len(nums) - i):
                if s + nums[i + j] > s:
                    s = s + nums[i + j]
        sum_list.append(s)
    return max(sum_list)


a = [-5, -1, 5, 7, 9, 11, -1, -10]
b = 4

print(find_maximal_subarray_sum(a, b))
