"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

"""


class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        nums = [i + 1 for i in range(n)]
        res = []
        self.dfs(nums, [], res, k, 0)
        return res

    def dfs(self, nums, path, res, k, index):
        if len(path) == k:
            res.append(path)
            return
        for i in range(index, len(nums)):
            self.dfs(nums, path + [nums[i]], res, k, i + 1)


test = Solution()
print(test.combine(4, 2))
