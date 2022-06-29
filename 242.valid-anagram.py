#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        dictS = defaultdict(int)
        dictT = defaultdict(int)

        for char in s:
            dictS[char] += 1
        for char in t:
            dictT[char] += 1

        if dictS == dictT:
            return True
        else:
            return False


# @lc code=end
