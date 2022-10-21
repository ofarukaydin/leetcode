#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
from functools import lru_cache


class Solution:
    def climbStairs(self, n: int) -> int:
        @lru_cache(maxsize=None)
        def aux(start, target):
            if start == target:
                return 1
            elif start > target:
                return 0

            return aux(start + 1, target) + aux(start + 2, target)

        return aux(0, n)


# @lc code=end
