"""
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Therefore, return the max sliding window as [3,3,5,5,6,7].

Note:
You may assume k is always valid, ie: 1 ≤ k ≤ input array's size for non-empty array.

Follow up:
Could you solve it in linear time?


"""

import collections


class Solution(object):
    # slow
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []

        dq = collections.deque(maxlen=k)

        res = []

        for i in range(len(nums)):
            dq.append(nums[i])
            if len(dq) == k:
                res.append(max(dq))

        return res

    #  fast excited
    def maxSlidingWindow2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        if not nums:
            return nums
        prevmax = max(nums[:k])
        res.append(prevmax)
        for i in range(k, len(nums)):
            if prevmax < nums[i]:
                prevmax = nums[i]
            elif prevmax != nums[i - k]:
                prevmax = max(nums[i], prevmax)
            else:
                prevmax = max(nums[i - k + 1:i + 1])
            res.append(prevmax)
        return res
