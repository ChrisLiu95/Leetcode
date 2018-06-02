"""
Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if not n:
            return []
        res = [[0 for _ in range(n)] for _ in range(n)]

        left = 0
        right = n - 1
        top = 0
        down = n - 1
        num = 1
        while left <= right and top <= down:
            for i in range(left, right + 1):
                res[top][i] = num
                num += 1
            top += 1

            for i in range(top, down + 1):
                res[i][right] = num
                num += 1
            right -= 1

            for i in range(right, left - 1, -1):
                res[down][i] = num
                num += 1
            down -= 1

            for i in range(down, top - 1, -1):
                res[i][left] = num
                num += 1
            left += 1

        return res
