# @before-stub-for-debug-begin
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=304 lang=python3
#
# [304] Range Sum Query 2D - Immutable
#

# @lc code=start


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.prefixSum = [
            [0 for _ in range(COLS+1)] for _ in range(ROWS+1)
        ]

        for row in range(ROWS):
            currSum = 0
            for col in range(COLS):
                currSum += matrix[row][col]
                prevSum = self.prefixSum[row][col + 1]
                self.prefixSum[row + 1][col + 1] = prevSum + currSum

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1+1, col1+1, row2+1, col2+1

        bottomRight = self.prefixSum[row2][col2]
        above = self.prefixSum[row1 - 1][col2]
        left = self.prefixSum[row2][col1 - 1]
        topLeft = self.prefixSum[row1 - 1][col1 - 1]

        return bottomRight - above - left + topLeft

    # Your NumMatrix object will be instantiated and called as such:
    # obj = NumMatrix(matrix)
    # param_1 = obj.sumRegion(row1,col1,row2,col2)
    # @lc code=end
