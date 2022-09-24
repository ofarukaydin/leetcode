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
        N = len(grid)
        minHeap = [(grid[0][0], 0, 0)]  # cost, r, c
        visited = set()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while minHeap:
            cost, row, col = heapq.heappop(minHeap)

            if row == N - 1 and col == N - 1:
                return cost

            if (row, col) not in visited:
                visited.add((row, col))

                for dr, dc in directions:
                    neiRow, neiCol = row + dr, col + dc
                    if (
                        neiRow < 0
                        or neiCol < 0
                        or neiRow == N
                        or neiCol == N
                        or (neiRow, neiCol) in visited
                    ):
                        continue

                    heapq.heappush(
                        minHeap, (max(cost, grid[neiRow][neiCol]), neiRow, neiCol))

        # @lc code=end
