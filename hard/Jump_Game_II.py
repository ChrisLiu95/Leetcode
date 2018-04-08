"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3
steps to the last index.)

"""


class Solution(object):
    # dp  time limit exceeded
    # dp[i] least step at current index
    def jump(self, nums):
        dp = [float("inf")] * len(nums)
        dp[0] = 0

        for i in range(1, len(nums)):
            for j in range(i):
                if i <= j + nums[j]:
                    dp[i] = min(dp[j] + 1, dp[i])
        return dp[-1]

    # greedy
    def jump2(self, nums):
        currMax = 0
        jump = 0
        end = 0

        for i in range(len(nums) - 1):
            currMax = max(currMax, i + nums[i])
            if i == end:
                jump += 1
                end = currMax
        return jump
