R#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
from functools import lru_cache

class Solution:
    def rob(self, nums: List[int]) -> int:

        @lru_cache(maxsize=None)
        def dfs(i, acc):
            if i >= len(nums):
                return acc

            return max(
                # We choose to rob so we skip to the i + 2th index
                dfs(i+2, acc + nums[i]),

                # We choose not to rob this index
                dfs(i+1, acc)
            )

        return dfs(0, 0)


# @lc code=end
