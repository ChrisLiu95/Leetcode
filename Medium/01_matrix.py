"""
Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.
Example 1:
Input:

0 0 0
0 1 0
0 0 0
Output:
0 0 0
0 1 0
0 0 0
Example 2:
Input:

0 0 0
0 1 0
1 1 1
Output:
0 0 0
0 1 0
1 2 1

"""


class Solution(object):
    def updateMatrix(self, matrix):

        queue, m, n = [], len(matrix), len(matrix[0])

        for i in range(m):
            for j in range(n):
                if not matrix[i][j]:
                    queue.append((i, j))
                else:
                    matrix[i][j] = float('inf')

        for x, y in queue:
            for r, c in ((x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)):
                step = matrix[x][y] + 1
                if 0 <= r < m and 0 <= c < n and matrix[r][c] > step:
                    matrix[r][c] = step
                    queue.append((r, c))
        return matrix
