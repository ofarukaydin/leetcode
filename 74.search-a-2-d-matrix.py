#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        start = 0
        end = (len(matrix) * len(matrix[0])) - 1

        while start <= end:
            middle = (start + end) // 2
            val = self.getMappedValue(middle, matrix)

            if target < val:
                end = middle - 1
            elif target > val:
                start = middle + 1
            else:
                return True

        return False

    def getMappedValue(self, indexToMap, matrix):
        colLen = len(matrix[0])

        if indexToMap == 0:
            return matrix[0][0]

        row = indexToMap // colLen
        col = indexToMap % colLen

        return matrix[row][col]


# @lc code=end
