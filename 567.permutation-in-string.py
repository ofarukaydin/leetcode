# @before-stub-for-debug-begin
from python3problem567 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start
import string


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        alphabet_string = string.ascii_lowercase
        alphabet_list = list(alphabet_string)
        s1Map = {}
        s2Map = {}
        matches = 0

        for char in alphabet_list:
            s1Map[char] = 0
            s2Map[char] = 0

        for i in range(len(s1)):
            s1Map[s1[i]] += 1
            s2Map[s2[i]] += 1

        for char in alphabet_list:
            if s1Map[char] == s2Map[char]:
                matches += 1

        l = 0
        for rightChar in s2[len(s1):len(s2)]:
            if matches == 26:
                return True

            wasRightEqual = s1Map[rightChar] == s2Map[rightChar]
            s2Map[rightChar] += 1
            if s2Map[rightChar] == s1Map[rightChar]:
                matches += 1
            elif wasRightEqual:
                matches -= 1

            leftChar = s2[l]
            wasLeftEqual = s1Map[leftChar] == s2Map[leftChar]
            s2Map[leftChar] -= 1
            if s2Map[leftChar] == s1Map[leftChar]:
                matches += 1
            elif wasLeftEqual:
                matches -= 1
            l += 1

        return matches == 26

# @lc code=end
