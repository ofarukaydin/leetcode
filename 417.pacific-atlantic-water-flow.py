#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#

# @lc code=start
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific, atlantic = set(), set()
        rows, cols = len(heights), len(heights[0])

        def dfs(row, col, visited, prevHeight):
            if (
                row < 0 or
                col < 0 or
                row >= rows or
                col >= cols or
                (row, col) in visited or
                heights[row][col] < prevHeight
            ):
                return
            visited.add((row, col))
            dfs(row, col + 1, visited, heights[row][col])
            dfs(row, col - 1, visited, heights[row][col])
            dfs(row + 1, col, visited, heights[row][col])
            dfs(row - 1, col, visited, heights[row][col])

        for col in range(cols):
            dfs(0, col, pacific, heights[0][col])
            dfs(rows - 1, col, atlantic, heights[rows - 1][col])

        for row in range(rows):
            dfs(row, 0, pacific, heights[row][0])
            dfs(row, cols - 1, atlantic, heights[row][cols - 1])

        res = []
        for row in range(rows):
            for col in range(cols):
                if (row, col) in atlantic and (row, col) in pacific:
                    res.append((row, col))
        return res

# @lc code=end
