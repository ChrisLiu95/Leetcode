"""
Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper
left corner (row1, col1) and lower right corner (row2, col2).

"""


class NumMatrix(object):

    def __init__(self, matrix):

        if not matrix:
            return
        self.matrix = matrix

    def sumRegion(self, row1, col1, row2, col2):

        sum = 0
        # r, c = len(self.matrix), len(self.matrix[0])
        for i in range(row1, row2 + 1):
            for j in range(col1, col2 + 1):
                sum += self.matrix[i][j]
        return sum
