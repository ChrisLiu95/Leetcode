"""
Given an array of integers, find out whether there are two distinct indices i and j in the array
such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between
i and j is at most k.

"""


class Solution(object):
    # 暴力解法 Brute Force Solution
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        for i in range(len(nums)):
            for j in range(i + 1, i + 1 + k):
                if j < len(nums):
                    if abs(nums[j] - nums[i]) <= t:
                        return True
        return False

    # bucket sort
    def containsNearbyAlmostDuplicate2(self, nums, k, t):
        if k < 1 or t < 0:
            return False

        maps = {}
        for i in range(len(nums)):
            keys = nums[i] / (t + 1)
            for ky in (keys, keys + 1, keys - 1):
                if ky in maps and i - maps[ky][0] <= k and abs(nums[i] - maps[ky][1]) <= t:
                    return True
            maps[keys] = (i, nums[i])

        return False
