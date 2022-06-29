# @before-stub-for-debug-begin
from python3problem76 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == '':
            return ''

        window, strMap = defaultdict(int), defaultdict(int)

        for c in t:
            strMap[c] += 1

        have, need = 0, len(strMap)

        l = 0
        res, resLen = [-1, -1], float('infinity')
        for r in range(len(s)):
            window[s[r]] += 1

            if s[r] in window and window[s[r]] == strMap[s[r]]:
                have += 1

            while have == need:
                if r-l+1 < resLen:
                    resLen = r-l+1
                    res = [l, r]

                window[s[l]] -= 1

                if s[l] in strMap and window[s[l]] < strMap[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l: r+1] if resLen != float('infinity') else ''

        # @lc code=end
