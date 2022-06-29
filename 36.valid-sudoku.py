# @before-stub-for-debug-begin
from collections import defaultdict
from python3problem36 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = defaultdict(set)
        cols = defaultdict(set)
        subBoards = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == '.':
                    continue
                subRow = i // 3
                subCol = j // 3
                if (
                    board[i][j] in rows[i] or
                    board[i][j] in cols[j] or
                    board[i][j] in subBoards[(subRow, subCol)]
                ):
                    return False
                else:
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    subBoards[(subRow, subCol)].add(board[i][j])

        return True


# @lc code=end
