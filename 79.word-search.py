#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        rows, cols = len(board), len(board[0])

        def dfs(row, col, index):
            if index == len(word):
                return True
            if (
                row < 0 or
                col < 0 or
                row >= rows or
                col >= cols or
                word[index] != board[row][col] or
                (row, col) in visited
            ):
                return False

            visited.add((row, col))
            res = (
                dfs(row + 1, col, index + 1) or
                dfs(row, col + 1, index + 1) or
                dfs(row - 1, col, index + 1) or
                dfs(row, col - 1, index + 1)
            )
            visited.remove((row, col))
            return res

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False


# @lc code=end
