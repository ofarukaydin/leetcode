# @before-stub-for-debug-begin
from python3problem3 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        left = 0
        length = float('-inf')

        for right in range(len(s)):
            while s[right] in window:
                window.remove(s[left])
                left += 1
            length = max(length, right - left + 1)

            window.add(s[right])

        return 0 if length == float('-inf') else length


# @lc code=end
