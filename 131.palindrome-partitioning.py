# @before-stub-for-debug-begin
from python3problem131 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#

# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def dfs(i, part):
            if i >= len(s):
                res.append(part.copy())
                return

            for j in range(i, len(s)):
                if self.isPalidrome(s[i:j+1]):
                    part.append(s[i: j + 1])
                    dfs(j + 1, part)
                    part.pop()

        dfs(0, [])
        return res

    def isPalidrome(self, s):
        l, r = 0, len(s) - 1

        while l <= r:
            if s[l] != s[r]:
                return False

            l += 1
            r -= 1

        return True


# @lc code=end
