"""
Given a sorted array and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 1:

Input: [1,3,5,6], 0
Output: 0

"""


class Solution(object):
    def search_insert(self, nums, target):
        res = 0
        if target < nums[0]:
            return 0
        if target > nums[len(nums) - 1]:
            return len(nums)
        for i in range(len(nums)):
            if nums[i] == target:
                res = i
            elif nums[i] < target < nums[i + 1]:
                res = i + 1
        return res

    def diff(self, nums, target):
        return len([x for x in nums if x < target])


test = Solution()
print(test.search_insert([1, 3], 4))
