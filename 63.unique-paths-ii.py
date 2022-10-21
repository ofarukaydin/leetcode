# @before-stub-for-debug-begin
from functools import lru_cache
from python3problem63 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#

# @lc code=start


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        OBSTACLE = 1

        @lru_cache(maxsize=None)
        def dfs(row, col):
            if row == ROWS or col == COLS or obstacleGrid[row][col] == OBSTACLE:
                return 0
            if row == ROWS - 1 and col == COLS - 1:
                return 1

            return dfs(row, col + 1) + dfs(row + 1, col)

        return dfs(0, 0)
# @lc code=end
