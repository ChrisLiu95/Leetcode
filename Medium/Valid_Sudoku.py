"""
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.


A partially filled sudoku which is valid.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated

"""


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        cell = [[] for _ in range(9)]
        Row = [[] for _ in range(9)]
        column = [[] for _ in range(9)]

        for i, row in enumerate(board):
            for j, num in enumerate(row):
                if num != ".":
                    k = (i // 3) * 3 + j // 3
                    if num in cell[k] or num in Row[i] or num in column[j]:
                        return False
                    cell[k].append(num)
                    Row[i].append(num)
                    column[j].append(num)
        return True
