# @before-stub-for-debug-begin
from functools import lru_cache
from python3problem309 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=309 lang=python3
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#

# @lc code=start


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        @lru_cache
        def dfs(i, buying):
            if i >= len(prices):
                return 0


            if buying:
                buying = dfs(i+1, False) - prices[i]
                cooldown = dfs(i+1, True)

                return max(buying, cooldown)
            else:
                sell = dfs(i+2, True) + prices[i]
                cooldown = dfs(i+1, False) # we cannot buy more than once

                return max(sell, cooldown)

        return dfs(0, True)

# @lc code=end
