"""
Given a list of integers numbers "nums".
You need to find a sub-array with length less equal to "k", with maximal sum.
The written function should return the sum of this sub-array.
Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    sum_list = []
    for i in range(len(nums)):
        sub_array = nums[i : i + k]
        local_sum = sub_array[0]
        for j in sub_array[1:]:
            if local_sum < local_sum + j:
                local_sum = local_sum + j
            sum_list.append(local_sum)
    return max(sum_list)
