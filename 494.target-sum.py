# @before-stub-for-debug-begin
from functools import lru_cache
from python3problem494 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#

# @lc code=start


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @lru_cache(maxsize=None)
        def dfs(i, total):
            if i >= len(nums):
                return 1 if total == target else 0

            return dfs(i+1, total + nums[i]) + dfs(i+1, total - nums[i])

        return dfs(0, 0)

        # @lc code=end
