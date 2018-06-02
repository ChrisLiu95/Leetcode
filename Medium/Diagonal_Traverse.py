"""
Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as
shown in the below image.

Example:
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output:  [1,2,4,7,5,3,6,8,9]

!! important, super complicated
"""


class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        if not matrix:
            return []

        m = len(matrix)
        n = len(matrix[0])
        res = []
        total = m * n
        step = 0

        if m <= 1 or n <= 1:
            for i in range(m):
                for j in range(n):
                    res.append(matrix[i][j])
            return res

        up_i, up_j = 0, 0
        down_i, down_j = 0, 1
        up = True

        while step < total:
            if up:
                i, j = up_i, up_j
                while i > -1 and j < n:
                    res.append(matrix[i][j])
                    i -= 1
                    j += 1
                    step += 1
                if up_i == m - 1:
                    up_j += 2
                elif up_i + 2 <= m - 1:
                    up_i += 2
                else:
                    up_i += 1
                    up_j += 1
            else:
                i, j = down_i, down_j
                while i < m and j > -1:
                    res.append(matrix[i][j])
                    i += 1
                    j -= 1
                    step += 1

                if down_j == n - 1:
                    down_i += 2
                elif down_j + 2 <= n - 1:
                    down_j += 2
                else:
                    down_i += 1
                    down_j += 1
            up = not up

        return res
