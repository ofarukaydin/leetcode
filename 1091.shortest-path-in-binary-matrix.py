#
# @lc app=leetcode id=1091 lang=python3
#
# [1091] Shortest Path in Binary Matrix
#

# @lc code=start
from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1

        ROWS, COLS = len(grid), len(grid[0])
        length = 0
        deq = deque()
        visited = set()

        deq.append((0, 0))
        visited.add((0, 0))

        while deq:
            length += 1
            for _ in range(len(deq)):
                row, col = deq.popleft()

                if (row, col) == (ROWS - 1, COLS - 1):
                    return length

                directions = [
                    [0, 1], [0, -1], [1, 0], [-1, 0],
                    [1, 1], [-1, -1], [1, -1], [-1, 1]
                ]

                for dx, dy in directions:
                    newRow, newCol = row + dx, col + dy
                    if (
                        newRow in range(ROWS) and
                        newCol in range(COLS) and
                        (newRow, newCol) not in visited and
                        grid[newRow][newCol] == 0
                    ):
                        deq.append((newRow, newCol))
                        visited.add((newRow, newCol))

        return -1

        # @lc code=end
