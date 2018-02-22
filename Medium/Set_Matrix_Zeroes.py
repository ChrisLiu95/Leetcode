"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

"""


class Solution(object):
    # slow O(mn)
    def setZeroes(self, matrix):
        # Two sets that record which row and column has 0
        rowSet = set()
        colSet = set()
        # Iterate each element.
        # If it is 0, record row and column number
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    rowSet.add(r)
                    colSet.add(c)
        # Change all rows containing 0 to 0
        for r in rowSet:
            for c in range(len(matrix[0])):
                matrix[r][c] = 0
        # Change all columns containing 0 to 0
        for c in colSet:
            for r in range(len(matrix)):
                matrix[r][c] = 0


test = Solution()
test.setZeroes([[1, 2, 0, 0, 5],
                [2, 0, 4, 5, 6],
                [1, 2, 6, 4, 0]])
