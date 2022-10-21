#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations = []

        def dfs(i, path):
            if len(path) == k:
                combinations.append(path.copy())
                return
            if i > n:
                return

            for j in range(i, n + 1):
                path.append(j)
                dfs(j+1, path)
                path.pop()

        dfs(1, [])

        return combinations


# @lc code=end
