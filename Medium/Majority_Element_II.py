"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
The algorithm should run in linear time and in O(1) space.

"""


class Solution(object):
    def majorityElement(self, nums):

        if not nums:
            return []
        mydir = {}
        res = set()
        for num in nums:
            mydir[num] = mydir.get(num, 0) + 1
        for num in nums:
            if mydir[num] > len(nums) // 3:
                res.add(num)
        return list(res)

