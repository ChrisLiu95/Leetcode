"""
Given an array of integers sorted in ascending order, find the starting and ending position
of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].


"""


class Solution(object):
    def searchRange(self, nums, target):
        if target not in nums:
            return [-1, -1]

        left, r = 0, len(nums) - 1
        res = [-1, -1]
        while left <= r and r > 0:
            if nums[left] != target:
                left += 1
            if nums[r] != target:
                r -= 1
            if nums[left] == target and nums[r] == target:
                res = [left, r]
                break
        if nums[r] == target and r == 0:
            return [0, 0]
        return res


test = Solution()
print(test.searchRange(8, [5, 7, 7, 8, 8, 10]))
