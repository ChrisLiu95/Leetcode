"""
Given an array S of n integers, find three integers in S such that the sum is closest to a given number,
target. Return the sum of the three integers. You may assume that each input would have exactly one
solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

"""


class Solution(object):
    def TSum_Closest(self, nums, target):
        nums.sort()
        length = len(nums)
        ans = 0
        cmp = float('inf')

        for i in range(length - 2):
            j = i + 1
            k = length - 1
            while j < k:
                value = nums[i] + nums[j] + nums[k]
                if value == target:
                    ans = value
                    return ans
                elif value > target:
                    k -= 1
                    if abs(target - value) < cmp:
                        cmp = abs(target - value)
                        ans = value
                else:
                    j += 1
                    if abs(target - value) < cmp:
                        cmp = abs(target - value)
                        ans = value
            return ans
