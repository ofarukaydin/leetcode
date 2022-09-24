# @before-stub-for-debug-begin
from python3problem695 import *
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
        res = 0
        maxRow = len(grid)
        maxCol = len(grid[0])
        visited = set()

        def dfs(row, col):
            if (
                row >= maxRow
                or col >= maxCol
                or row < 0
                or col < 0
                or grid[row][col] == 0
                or (row, col) in visited
            ):
                return 0

            visited.add((row, col))

            area = (1
                    + dfs(row, col + 1)
                    + dfs(row, col - 1)
                    + dfs(row + 1, col)
                    + dfs(row - 1, col)
                    )

            return area

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                res = max(res, dfs(row, col))
        return res


# @lc code=end
