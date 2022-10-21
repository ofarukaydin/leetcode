# @before-stub-for-debug-begin
from python3problem200 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        visited = set()
        ROWS, COLS = len(grid), len(grid[0])
        res = 0

        def dfs(row, col):
            if (
                row not in range(ROWS) or
                col not in range(COLS) or
                grid[row][col] == '0' or
                (row, col) in visited
            ):
                return

            visited.add((row, col))

            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == '1' and (row, col) not in visited:
                    res += 1
                dfs(row, col)
        return res


# @lc code=end
