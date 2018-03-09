"""
Given an array of n positive integers and a positive integer s, find the minimal length of a
contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.

"""


class Solution:
    # @param {integer} s
    # @param {integer[]} nums
    # @return {integer}
    def minSubArrayLen(self, s, nums):
        start, end, total = 0, 0, 0
        size = len(nums)
        res = size + 1

        while end < size:
            while end < size and total < s:
                total += nums[end]
                end += 1
            while start < end and total >= s:
                res = min(res, end - start)
                total -= nums[start]
                start += 1
        return [0, res][res <= size]

    def minSibArrayLen2(self, s, nums):

        m = len(nums)
        left = 0
        k = m + 1

        sum = 0
        for i in range(m):
            sum += nums[i]
            while sum >= s:
                k = min(k, i - left + 1)
                sum -= nums[left]
                left += 1

        return k if k != m + 1 else 0
