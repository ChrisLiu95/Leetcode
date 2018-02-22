"""
Given an array of integers, every element appears three times except for one, which appears exactly once.
Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

"""
import collections


class Solution(object):
    def singleNumber(self, nums):
        counter = collections.Counter(nums)
        for key, value in counter.items():
            if value == 1:
                return key
        return False


test = Solution()
print(test.singleNumber([2, 2, 2, 3]))
