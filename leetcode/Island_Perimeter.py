"""
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.
Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water,
and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes"
(water inside that isn't connected to the water around the island). One cell is a square with side length 1.
The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

"""


class Solution(object):
    def islandPerimeter(self, grid):
        row = len(grid)
        column = len(grid[0])
        res = 0
        for i in range(row):
            for j in range(column):
                if grid[i][j] == 1:
                    res += 4
                    if i < row - 1 and grid[i + 1][j] == 1:
                        res -= 2
                    if j < column - 1 and grid[i][j + 1] == 1:
                        res -= 2

        return res

    # 暴力解法
    def solution2(self, grid):
        n = len(grid)
        m = len(grid[0])
        perm = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    if i - 1 >= 0 and grid[i - 1][j] == 0:
                        perm += 1
                    if i + 1 < n and grid[i + 1][j] == 0:
                        perm += 1
                    if j - 1 >= 0 and grid[i][j - 1] == 0:
                        perm += 1
                    if j + 1 < m and grid[i][j + 1] == 0:
                        perm += 1
                    if i == 0:
                        perm += 1
                    if i == n - 1:
                        perm += 1
                    if j == 0:
                        perm += 1
                    if j == m - 1:
                        perm += 1
        return perm


test = Solution()
print(test.islandPerimeter([[0, 1, 0, 0],
                            [1, 1, 1, 0],
                            [0, 1, 0, 0],
                            [1, 1, 0, 0]]))
