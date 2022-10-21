#
# @lc app=leetcode id=329 lang=python3
#
# [329] Longest Increasing Path in a Matrix
#

# @lc code=start


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = {}

        def dfs(i, j, prevVal):
            if (
                i not in range(0, rows)
                or j not in range(0, cols)
                or matrix[i][j] <= prevVal
            ):
                return 0
            if (i, j) in dp:
                return dp[(i, j)]

            res = 1
            res = max(res, 1 + dfs(i + 1, j, matrix[i][j]))
            res = max(res, 1 + dfs(i - 1, j, matrix[i][j]))
            res = max(res, 1 + dfs(i, j + 1, matrix[i][j]))
            res = max(res, 1 + dfs(i, j - 1, matrix[i][j]))
            dp[(i, j)] = res

            return res

        for row in range(rows):
            for col in range(cols):
                dfs(row, col, -1)

        return max(dp.values())
# @lc code=end
