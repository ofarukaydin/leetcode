#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        combinations = []

        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(i, currStr):
            if len(digits) == len(currStr):
                combinations.append(currStr)
                return

            for char in digitToChar[digits[i]]:
                backtrack(i+1, currStr + char)

        if digits:
            backtrack(0, '')

        return combinations


# @lc code=end
