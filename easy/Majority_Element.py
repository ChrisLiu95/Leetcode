"""

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

"""
from collections import Counter


class Solution(object):

    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = Counter(nums)
        res = counter.most_common()[0][0]
        return res

    # NOTICE that the majority element always exist in the array,so that the middle always is the answer
    # much faster!
    def majorityElement2(self, nums):
        return sorted(nums)[int(len(nums) / 2)]



test = Solution()
print(test.majorityElement([1, 1, 1, 1, 1, 1, 2, 2, 2, 4, 5, 6]))
