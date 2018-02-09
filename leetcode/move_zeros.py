"""
ali 面试

Given an array nums, write a function to move all 0's to the end of it
while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.

283
"""


class Solution(object):
    def ali(self, nums):
        j = 0
        for i in range(len(nums)):
            if nums[i] is not 0:
                nums[j] = nums[i]
                j = j + 1
        for k in range(j, len(nums)):
            nums[k] = 0
        return nums


test = Solution()
print(test.ali([0, 1, 0, 3, 2]))
