# @before-stub-for-debug-begin
from python3problem17 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []

        def dfs(i, currStr):
            if i >= len(digits):
                if currStr:
                    res.append(currStr)
                return

            digitAsChar = digits[i]
            for c in digitMap[digitAsChar]:
                dfs(i+1, currStr + c)

        dfs(0, '')

        return res
# @lc code=end
