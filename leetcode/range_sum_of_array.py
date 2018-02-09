"""
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
"""


class Solution(object):

    def __init__(self, nums):
        self.nums = nums

    def range_sum(self, i, j):
        length = len(self.nums)
        for index in range(1, length):
            self.nums[index] += self.nums[index-1]

        return self.nums[j]-self.nums[i-1]


test = Solution([1, 2, 3, 4, 5])
print(test.range_sum(1, 3))
