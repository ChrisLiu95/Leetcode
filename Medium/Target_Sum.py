"""
You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols +
and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:
Input: nums is [1, 1, 1, 1, 1], S is 3.
Output: 5
Explanation:

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.

Pick a data structure(dictionary) dic: dic[i] = j denotes that with given target sum i,
there are j ways reaching to it.
"""


class Solution(object):
    def findTargetSumWays(self, nums, S):
        # dir = {nums[0]: 1, -nums[0]: 1} if nums[0] != 0 else {0: 2}
        dir = {0: 1}
        for num in nums:
            temp = {}
            for key in dir:
                temp[key + num] = temp.get(key + num, 0) + dir.get(key, 0)
                temp[key - num] = temp.get(key - num, 0) + dir.get(key, 0)
            dir = temp
        return dir[S]
