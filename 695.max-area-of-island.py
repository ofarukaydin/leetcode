# @before-stub-for-debug-begin
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#

# @lc code=start


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])
        res = 0

        def dfs(row, col):
            if (
                row not in range(ROWS) or
                col not in range(COLS) or
                grid[row][col] == 0 or
                (row, col) in visited
            ):
                return 0

            visited.add((row, col))

            return (1
                    + dfs(row + 1, col)
                    + dfs(row - 1, col)
                    + dfs(row, col + 1)
                    + dfs(row, col - 1)
                    )

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1 and (row, col) not in visited:
                    res = max(res, dfs(row, col))
        return res
# @lc code=end
