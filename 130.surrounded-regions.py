# @before-stub-for-debug-begin
from python3problem130 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#

# @lc code=start


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        maxRows, maxCols = len(board), len(board[0])

        def dfs(row, col):
            if (
                row >= maxRows
                or col >= maxCols
                or row < 0
                or col < 0
                or board[row][col] != 'O'
            ):
                return

            board[row][col] = 'T'
            dfs(row, col + 1)
            dfs(row, col - 1)
            dfs(row + 1, col)
            dfs(row - 1, col)

        for row in range(maxRows):
            for col in range(maxCols):
                if board[row][col] == 'O' and (row in [0, maxRows - 1] or col in [0, maxCols - 1]):
                    dfs(row, col)

        for row in range(maxRows):
            for col in range(maxCols):
                if board[row][col] == "O":
                    board[row][col] = 'X'

        for row in range(maxRows):
            for col in range(maxCols):
                if board[row][col] == 'T':
                    board[row][col] = 'O'


# @lc code=end
