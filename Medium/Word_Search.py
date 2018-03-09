"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those
horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example,
Given board =

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.


"""


# encountered LTE problem

class Solution(object):
    def exist(self, board, word):
        m, n, index = len(board), len(board[0]), 0

        def dfs(i, j, k):
            if 0 <= i < m and 0 <= j < n and board[i][j] == word[k]:
                if k == len(word) - 1:
                    return True
                else:
                    temp = board[i][j]
                    board[i][j] = '#'
                    res = dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i + 1, j, k + 1) or dfs(i, j - 1, k + 1)
                    board[i][j] = temp
                    return res
            return False

        for x in range(m):
            for y in range(n):
                if dfs(x, y, index):
                    return True
        return False


test = Solution()
print(test.exist([
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
], "ASADFBE"))
