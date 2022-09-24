# @before-stub-for-debug-begin
import math
from python3problem875 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#

# @lc code=start
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        k = 0

        while left <= right:
            middle = (left + right) // 2
            totalHours = 0

            for p in piles:
                totalHours += math.ceil(p / middle)

            if totalHours <= h:
                k = middle
                right = middle - 1
            else:
                left = middle + 1

        return k


# @lc code=end
