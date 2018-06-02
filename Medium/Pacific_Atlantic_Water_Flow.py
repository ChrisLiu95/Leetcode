"""
感觉是经典题= =

Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent,
the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right
and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

Note:
The order of returned grid coordinates does not matter.
Both m and n are less than 150.
Example:

Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).

用两个set分别记录从pacific还有atlantic符合的路径，然后比较两个set，相同的坐标加入res。
反向dfs，从pacific还有atlantic边界开始dfs， excited
"""


class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix:
            return []

        res = []
        m = len(matrix)
        n = len(matrix[0])

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def Pacific(matrix):
            visited = set()
            for j in range(n):
                dfs(matrix, 0, j, visited)
            for i in range(m):
                dfs(matrix, i, 0, visited)
            return visited

        def Atlantic(matrix):
            visited = set()
            for i in range(m):
                dfs(matrix, i, n - 1, visited)
            for j in range(n):
                dfs(matrix, m - 1, j, visited)
            return visited

        def dfs(matrix, i, j, visited):
            if (i, j) in visited:
                return
            visited.add((i, j))
            for direction in directions:
                next_i = i + direction[0]
                next_j = j + direction[1]
                if 0 <= next_i < m and 0 <= next_j < n and matrix[next_i][next_j] >= matrix[i][j]:
                    dfs(matrix, next_i, next_j, visited)

        pacific = Pacific(matrix)
        atlantic = Atlantic(matrix)

        for i, j in pacific:
            if (i, j) in atlantic:
                res.append([i, j])
        return res
