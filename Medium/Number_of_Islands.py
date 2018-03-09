"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or
vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

11110
11010
11000
00000
Answer: 1

Example 2:

11000
11000
00100
00011
Answer: 3

"""


class Solution(object):
    def numIslands(self, grid):

        # 记得加边界条件

        if not grid:
            return 0
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            if 0 <= i < m and 0 <= j < m and grid[i][j]:
                grid[i][j] = 0
                dfs(i - 1, j)
                dfs(i + 1, j)
                dfs(i, j + 1)
                dfs(i, j - 1)
            else:
                return

        count = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c]:
                    dfs(r, c)
                    count += 1

        return count
