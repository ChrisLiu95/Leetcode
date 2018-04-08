"""
In a given integer array nums, there is always exactly one largest element.

Find whether the largest element in the array is at least twice as much as every other number in the array.

If it is, return the index of the largest element, otherwise return -1.

Example 1:

Input: nums = [3, 6, 1, 0]
Output: 1
Explanation: 6 is the largest integer, and for every other number in the array x,
6 is more than twice as big as x.  The index of value 6 is 1, so we return 1.


Example 2:

Input: nums = [1, 2, 3, 4]
Output: -1
Explanation: 4 isn't at least as big as twice the value of 3, so we return -1.

"""


class Solution(object):
    def dominantIndex(self, nums):
        if len(nums) == 1:
            return 0
        ans = [-float("inf"), 0, -float("inf")]

        for i, num in enumerate(nums):
            if num > ans[0]:
                ans[2] = ans[0]
                ans[0] = num
                ans[1] = i
            elif num > ans[2]:
                ans[2] = num

        if (ans[2] != 0 and ans[0] / ans[2] >= 2) or ans[2] == 0:
            return ans[1]
        return -1
