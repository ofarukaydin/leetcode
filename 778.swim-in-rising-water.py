# @before-stub-for-debug-begin
from python3problem778 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=778 lang=python3
#
# [778] Swim in Rising Water
#

# @lc code=start
import heapq


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        minHeap = [(grid[0][0], 0, 0)]  # (elevation, (row, col))
        visited = set()
        time = 0
        visited.add((0, 0))

        while minHeap:
            while minHeap and minHeap[0][0] <= time:
                elevation, row, col = heapq.heappop(minHeap)

                if grid[row][col] == grid[-1][-1]:
                    return time

                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

                for dr, dc in directions:
                    newRow = dr + row
                    newCol = dc + col
                    if (
                        newRow in range(rows) and
                        newCol in range(cols) and
                        (newRow, newCol) not in visited
                    ):
                        visited.add((newRow, newCol))
                        heapq.heappush(
                            minHeap, (max(elevation, grid[newRow][newCol]), newRow, newCol))
            time += 1


# @lc code=end
