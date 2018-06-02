"""
Given a non-empty array containing only positive integers, find if the array can be partitioned
into two subsets such that the sum of elements in both subsets is equal.

Note:
Each of the array element will not exceed 100.
The array size will not exceed 200.
Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.

"""


class Solution(object):
    # LTE, compute all possible solution, slow
    def canPartition(self, nums):
        if sum(nums) % 2 == 1:
            return False
        else:
            res = []
            self.dfs(nums, 0, [], res)
            print(res)
            for item in res:
                if sum(item) == sum(nums) / 2:
                    return True
            return False

    def dfs(self, nums, index, path, res):
        if sum(path) > sum(nums) / 2:
            return
        res.append(path)
        for i in range(index, len(nums)):
            self.dfs(nums, i + 1, path + [nums[i]], res)


test = Solution()
test.canPartition([1, 5, 11, 5])
