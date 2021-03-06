"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the
matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].

"""


class Solution():
    def spiralOrder(self, matrix):
        if not matrix:
            return []
        up, left = 0, 0
        right, down = len(matrix[0]) - 1, len(matrix) - 1
        direction = 0  # 0: go right   1: go down  2: go left  3: go up
        res = []

        while True:
            if direction == 0:
                for i in range(left, right + 1):
                    res.append(matrix[up][i])
                up += 1
            if direction == 1:
                for i in range(up, down + 1):
                    res.append(matrix[i][right])
                right -= 1
            if direction == 2:
                for i in range(right, left - 1, -1):
                    res.append(matrix[down][i])
                down -= 1
            if direction == 3:
                for i in range(down, up - 1, -1):
                    res.append(matrix[i][left])
                left += 1
            if up > down or left > right:
                return res
            direction = (direction + 1) % 4

