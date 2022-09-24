# @before-stub-for-debug-begin
from collections import deque
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#

# @lc code=start


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        maxRows, maxCols = len(grid), len(grid[0])
        deq = deque()
        time = 0
        fresh = 0

        for row in range(maxRows):
            for col in range(maxCols):
                if grid[row][col] == 2:
                    deq.append((row, col))
                elif grid[row][col] == 1:
                    fresh += 1

        directions = [[0, -1], [0, 1], [1, 0], [-1, 0]]
        while deq and fresh > 0:
            rottenOranges = len(deq)

            for _ in range(rottenOranges):
                r, c = deq.popleft()

                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    # if in bounds and nonrotten, make rotten
                    # and add to q
                    if (
                        row in range(len(grid))
                        and col in range(len(grid[0]))
                        and grid[row][col] == 1
                    ):
                        grid[row][col] = 2
                        deq.append((row, col))
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1

# @lc code=end
