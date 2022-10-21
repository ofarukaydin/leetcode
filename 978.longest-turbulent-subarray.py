# @before-stub-for-debug-begin
from python3problem978 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=978 lang=python3
#
# [978] Longest Turbulent Subarray
#

# @lc code=start


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        arrLen = len(arr)
        ans = 1
        left = 0

        for right in range(1, arrLen):
            compareWithBefore = self.cmp(arr[right-1], arr[right])

            # They're the same element so we move left
            if compareWithBefore == 0:
                left = right

            # we compare right pointer with its left and right neighbors and if they have flipping signs,
            # we continue the loop and increment right poiner
            # if they have the same sign, we just update left pointer
            # and also update left if we're at the end of the iteration
            elif right == arrLen-1 or compareWithBefore * self.cmp(arr[right], arr[right+1]) != -1:
                ans = max(ans, right - left + 1)
                left = right
        return ans

    def cmp(self, a, b):
        if a > b:
            return 1
        elif a < b:
            return -1
        else:
            return 0

# @lc code=end
