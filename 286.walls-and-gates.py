#
# @lc app=leetcode id=286 lang=python3
#
# [286] Walls and Gates
#

# @lc code=start
from collections import deque


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        maxRows, maxCols = len(rooms), len(rooms[0])
        visited = set()
        deq = deque()

        for row in range(maxRows):
            for col in range(maxCols):
                if rooms[row][col] == 0:
                    deq.append((row, col))
                    visited.add((row, col))

        def addRoom(row, col):
            if (
                row >= maxRows
                or col >= maxCols
                or row < 0
                or col < 0
                or rooms[row][col] == -1
                or (row, col) in visited
            ):
                return

            visited.add((row, col))
            deq.append((row, col))

        distance = 0
        while deq:
            deqLen = len(deq)

            for _ in range(deqLen):
                row, col = deq.popleft()
                rooms[row][col] = distance

                addRoom(row + 1, col)
                addRoom(row - 1, col)
                addRoom(row, col + 1)
                addRoom(row, col - 1)

            distance += 1


# @lc code=end
