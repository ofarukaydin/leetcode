#
# @lc app=leetcode id=97 lang=python3
#
# [97] Interleaving String
#

# @lc code=start
from functools import lru_cache


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        @lru_cache(maxsize=None)
        def dfs(i, j):
            if i == len(s1) and j == len(s2):
                return True

            if i < len(s1) and s1[i] == s3[i + j] and dfs(i + 1, j):
                return True
            if j < len(s2) and s2[j] == s3[i + j] and dfs(i, j + 1):
                return True

            return False

        return dfs(0, 0)

# @lc code=end
