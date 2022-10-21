# @before-stub-for-debug-begin
from python3problem424 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        maxLen = 0
        maxFrequent = 0
        count = defaultdict(int)

        for right in range(len(s)):
            count[s[right]] += 1
            maxFrequent = max(maxFrequent, count[s[right]])

            while (right - left + 1) - maxFrequent > k:
                count[s[left]] -= 1
                left += 1

            maxLen = max(maxLen, right - left + 1)

        return maxLen


# @lc code=end
