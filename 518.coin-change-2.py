#
# @lc app=leetcode id=518 lang=python3
#
# [518] Coin Change II
#

# @lc code=start


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}

        def dfs(i, curr):
            if curr == amount:
                return 1
            if i >= len(coins):
                return 0
            if curr > amount:
                return 0
            if (i, curr) in cache:
                return cache[(i, curr)]

            cache[(i, curr)] = dfs(i, curr + coins[i]) + dfs(i+1, curr)
            return cache[(i, curr)]

        return dfs(0, 0)


# @lc code=end
