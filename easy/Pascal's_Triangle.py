"""
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

Pascal's triangle: a triangular array of numbers in which those at the ends of the rows are 1 and each of the others is the sum of the
nearest two numbers in the row above (the apex, 1, being at the top).

"""


class Solution:
    def generate(self, numRows):
        if not numRows:
            return []
        res = [[1]]
        for i in range(1, numRows):
            res.append([0] * (i + 1))
            for j in range(i + 1):
                if j == 0 or j == i:
                    res[i][j] = 1
                else:
                    res[i][j] = res[i - 1][j - 1] + res[i - 1][j]
        return res
