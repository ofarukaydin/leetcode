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
from collections import deque


class Solution:


    def numIslands(self, grid: List[List[str]]) -> int:

        visited = set()
        islands = 0
        rowLen = range(len(grid))
        colLen = range(len(grid[0]))

        def bfs(row, column):
            queue = deque()
            directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
            queue.append((row, column))

            while queue:
                (row, column) = queue.popleft()

                for deltaRow, deltaColumn in directions:
                    rowToVisit, columnToVisit = row + deltaRow, column + deltaColumn
                    if (rowToVisit in rowLen and
                        columnToVisit in colLen and
                        grid[rowToVisit][columnToVisit] == '1' and
                        (rowToVisit, columnToVisit) not in visited
                        ):
                        queue.append((rowToVisit, columnToVisit))
                    visited.add((rowToVisit, columnToVisit))

        for row in rowLen:
            for column in colLen:
                if grid[row][column] == '1' and (row, column) not in visited:
                    bfs(row, column)
                    islands += 1
                visited.add((row, column))

        return islands






# @lc code=end
