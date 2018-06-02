"""
Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the character '.'.

You may assume that there will be only one unique solution.

"""


class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        self.helper(board)

    def helper(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    for k in range(1, 10):
                        if self.isvalid(board):
                            board[i][j] = str(k)
                            if self.helper(board):
                                return True
                            else:
                                board[i][j] = "."
                    return False
        return True

    def isvalid(self, board):
        row = [[] for _ in range(9)]
        column = [[] for _ in range(9)]
        cell = [[] for _ in range(9)]

        for i, r in enumerate(board):
            for j, num in enumerate(r):
                k = (i // 3) * 3 + (j // 3)
                if num in row[i] or num in column[j] or num in cell[k]:
                    return False
                row[i].append(num)
                column[j].append(num)
                cell[k].append(num)
        return True
