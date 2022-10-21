# @before-stub-for-debug-begin
from python3problem875 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#

# @lc code=start
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = max(piles)

        while l <= r:
            k = (l + r) // 2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(p / k)

            if totalTime <= h:
                r = k - 1
                res = k
            else:
                l = k + 1
        return res


# @lc code=end
