#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        length = len(matrix) * len(matrix[0])
        l, r = 0, length - 1

        while l <= r:
            m = (l + r) // 2
            if self.getValFromMatrix(matrix, m) > target:
                r = m - 1
            elif self.getValFromMatrix(matrix, m) < target:
                l = m + 1
            else:
                return True

        return False

    def getValFromMatrix(self, matrix, i):
        rowLen, colLen = len(matrix), len(matrix[0])
        row = i // colLen
        col = i % colLen

        return matrix[row][col]

        # @lc code=end
