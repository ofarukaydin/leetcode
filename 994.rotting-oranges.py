# @before-stub-for-debug-begin
from python3problem994 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#

# @lc code=start
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        ROWS, COLS = len(grid), len(grid[0])
        freshOranges = 0
        time = 0

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2:
                    queue.append((row, col))
                if grid[row][col] == 1:
                    freshOranges += 1

        while freshOranges > 0 and queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

                for dx, dy in directions:
                    newRow, newCol = dx + row, dy + col

                    if (
                        newRow in range(ROWS) and
                        newCol in range(COLS) and
                        grid[newRow][newCol] == 1
                    ):
                        queue.append((newRow, newCol))
                        grid[newRow][newCol] = 2
                        freshOranges -= 1
            time += 1

        return time if freshOranges == 0 else -1


# @lc code=end
