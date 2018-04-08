"""
Given an array consisting of n integers, find the contiguous subarray of given length
k that has the maximum average value. And you need to output the maximum average value.

Example 1:
Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75

Note:
1 <= k <= n <= 30,000.
Elements of the given array will be in the range [-10,000, 10,000].

"""

from collections import deque


class Solution(object):
    def findMaxAverage(self, nums, k):
        dq = deque(maxlen=k)
        res = float("inf")
        for num in nums:
            dq.append(num)
            res = max(res, sum(dq) / len(dq))
        return res

    def findMaxAverage2(self, nums, k):
        total = sum(nums[:k])
        res = total

        for i in range(k, len(nums)):
            total += nums[i] - nums[i - k]
            if total > res:
                res = total
        return float(res) / k
