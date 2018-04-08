"""
Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may
NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

nums = [
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
Return 4
The longest increasing path is [1, 2, 6, 9].

Example 2:

nums = [
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
Return 4
The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

"""


class Solution(object):
    # no bug clear version
    def longestIncreasingPath(self, matrix):
        if not matrix:
            return 0
        res = 0
        m = len(matrix)
        n = len(matrix[0])
        cache = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                temp = self.dfs(matrix, -float("inf"), i, j, m, n, cache)
                res = max(res, temp)
        return res

    def dfs(self, matrix, min, i, j, m, n, cache):
        if i < 0 or i >= m or j < 0 or j >= n or matrix[i][j] <= min:
            return 0
        if cache[i][j] != 0:
            return cache[i][j]
        min = matrix[i][j]
        a = self.dfs(matrix, min, i + 1, j, m, n, cache) + 1
        b = self.dfs(matrix, min, i - 1, j, m, n, cache) + 1
        c = self.dfs(matrix, min, i, j + 1, m, n, cache) + 1
        d = self.dfs(matrix, min, i, j - 1, m, n, cache) + 1

        cache[i][j] = max(a, b, c, d)
        return cache[i][j]

    def longestIncreasingPath2(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        # idea is to go left right up down and compute the value.
        # if we go out of bound then return 0
        # store max increasing path for each vertex i, j.
        # if we visit that vertex again somehow then simply return that value instead of recomputing it
        # take example [1,2,3] and try to run the code
        # memo table
        self.memo = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.dfs(matrix, i, j, -1)
        if not self.memo:
            return 0
        return max(self.memo.values())

    def dfs(self, matrix, i, j, last):
        # edge condition
        if 0 <= i < len(matrix) and 0 <= j < len(matrix[0]) and last < matrix[i][j]:
            # if data in memo return
            if (i, j) in self.memo:
                return self.memo[(i, j)]
            # store each i,j value in memo with max of the path for given i,j
            self.memo[(i, j)] = 1 + max(self.dfs(matrix, i + 1, j, matrix[i][j]),
                                        self.dfs(matrix, i - 1, j, matrix[i][j]),
                                        self.dfs(matrix, i, j + 1, matrix[i][j]),
                                        self.dfs(matrix, i, j - 1, matrix[i][j]))
            # return the value to upper recursive function
            return self.memo[(i, j)]

        else:
            # if out of bound return 0. because length will be zero for that i, j
            return 0
