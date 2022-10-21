#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#

# @lc code=start
from functools import lru_cache


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        @lru_cache(maxsize=None)
        def dfs(i, j):
            if i == len(word1) and j == len(word2):
                return 0
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i

            if word1[i] == word2[j]:
                return dfs(i+1, j+1)
            else:
                return 1 + min(
                    dfs(i+1, j+1),  # replace
                    dfs(i+1, j),  # delete
                    dfs(i, j+1)  # insert
                )

        return dfs(0, 0)


# @lc code=end
