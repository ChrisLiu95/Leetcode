"""
Given an array nums and a target value k, find the maximum length of a sub_array that sums to k.
If there isn't one, return 0 instead.

Note:
The sum of the entire nums array is guaranteed to fit within the 32-bit signed integer range.

Example 1:
Given nums = [1, -1, 5, -2, 3], k = 3,
return 4. (because the subarray [1, -1, 5, -2] sums to 3 and is the longest)

"""


# 暴力解法
def solution(nums, k):
    result = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            curr = nums[i:j + 1]
            if sum(curr) == k:
                result.append(nums[i:j + 1])

    if len(result) == 0:
        return 0

    return max([len(i) for i in result])


class Solution(object):
    def subarray_size(self, nums, k):
        result, acc = 0, 0
        dic = {0: -1}

        for i in range(len(nums)):
            acc += nums[i]
            if acc not in dic:
                dic[acc] = i
            if acc - k in dic:
                result = max(result, i - dic[acc - k])

        return result
