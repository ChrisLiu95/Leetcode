"""
Given two sparse matrices A and B, return the result of AB.

You may assume that A's column number is equal to B's row number.

Sparse matrix:
a sparse matrix or sparse array is a matrix in which most of the elements are zero.
"""


class Solution(object):
    def multiply(self, A, B):
        mA, nA, nB = len(A), len(A[0]), len(B[0])
        res = [[0] * len(B[0]) for _ in range(mA)]
        for i in range(mA):
            for j in range(nA):
                if A[i][j]:
                    for k in range(nB):
                        res[i][k] += A[i][j] * B[j][k]
        return res


test = Solution()
print(test.multiply([
    [1, 0, 0],
    [-1, 0, 3]
], [
    [7, 0, 0],
    [0, 0, 0],
    [0, 0, 1]
]
))
