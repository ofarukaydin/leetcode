#
# @lc app=leetcode id=115 lang=python3
#
# [115] Distinct Subsequences
#

# @lc code=start
from functools import lru_cache


class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        @lru_cache(maxsize=None)
        def dfs(i, j):
            if j == len(t):
                return 1
            elif i == len(s):
                return 0

            if s[i] == t[j]:
                return dfs(i+1, j+1) + dfs(i+1, j)
            else:
                return dfs(i+1, j)

        return dfs(0, 0)

# @lc code=end
