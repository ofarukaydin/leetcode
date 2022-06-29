# @before-stub-for-debug-begin
from python3problem3 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=3 lang=python3
#x§
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        leftPointer, rightPointer = 0, 0
        maxLength = 0
        substrSet = set()

        while rightPointer < len(s):
            while s[rightPointer] in substrSet:
                substrSet.remove(s[leftPointer])
                leftPointer += 1
            substrSet.add(s[rightPointer])
            maxLength = max(maxLength, rightPointer - leftPointer + 1)
            rightPointer += 1
        return maxLength




            

            

        
# @lc code=end

