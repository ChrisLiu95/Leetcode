"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.

"""


class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[1])
        i, j = 0, m - 1
        while i <= j and i < m and j < m:
            mid = (i + j) >> 1
            if target > matrix[mid][n - 1]:
                i = mid + 1
            elif target < matrix[mid][n - 1]:
                j = mid - 1
            else:
                return True
        if i >= m:  # 判断是否越界
            return False
        row = i
        i, j = 0, n - 1
        while i <= j and i < n and j < n:
            mid = (i + j) >> 1
            if target > matrix[row][mid]:
                i = mid + 1
            elif target < matrix[row][mid]:
                j = mid - 1
            else:
                return True
        return False


test = Solution()
print(test.searchMatrix([
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
], 23))
