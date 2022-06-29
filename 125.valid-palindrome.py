# @before-stub-for-debug-begin
from python3problem125 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        startIndex = 0
        endIndex = len(s) - 1

        while startIndex < endIndex:
            while not s[startIndex].isalnum() and startIndex < endIndex:
                startIndex += 1

            while not s[endIndex].isalnum() and endIndex > startIndex:
                endIndex -= 1

            if s[startIndex].lower() != s[endIndex].lower():
                return False

            startIndex += 1
            endIndex -= 1

        return True


# @lc code=end
