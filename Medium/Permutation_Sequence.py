"""
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:

Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.
Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"

"""

from itertools import permutations


class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # LTE
        nums = [str(i + 1) for i in range(n)]
        res = []
        self.dfs(nums, "", res, k)
        return res[-1]

    def dfs(self, nums, path, res, k):
        if not nums:
            if len(res) == k:
                return
            res.append(path)
        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i + 1:], path + nums[i], res, k)

    def getPermutation2(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        permutation = permutations(range(1, n + 1))
        while k > 0:
            res = next(permutation)
            k -= 1
        return ''.join([str(i) for i in res])


test = Solution()
print(test.getPermutation2(3, 3))
