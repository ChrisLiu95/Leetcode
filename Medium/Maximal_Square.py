"""
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only
1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 4.

"""


class Solution(object):

    def maximalSquare(self, matrix):
        if not matrix:
            return 0
        r, c = len(matrix), len(matrix[0])
        dp = [[1 if matrix[r][c] else 0 for c in range(c)] for r in range(r)]
        # print(dp)
        for i in range(1, r):
            for j in range(1, c):
                if matrix[i][j]:
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
        return (max(max(r) for r in dp))**2


test = Solution()
print(test.maximalSquare([[1, 0, 1, 0, 0], [1, 0, 1, 1, 1], [1, 1, 1, 1, 1], [1, 0, 0, 1, 0]]))
