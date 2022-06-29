# @before-stub-for-debug-begin
from collections import defaultdict
from python3problem322 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start


class Solution:
    def __init__(self):
        self.cache = defaultdict()
        self.cache.default_factory = lambda: float('inf')

    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0

        for coin in coins:
            self.cache[coin] = 1

        res = self.change(coins, amount)

        return res if res != float('inf') else -1

    def change(self, coins: List[int], amount: int):
        if amount in self.cache:
            return self.cache[amount]

        for coin in coins:
            remainingAmount = amount - coin
            if remainingAmount >= 0:
                change = 1 + self.change(coins, remainingAmount)
                self.cache[amount] = min(self.cache[amount], change)

        return self.cache[amount]


# @lc code=end
