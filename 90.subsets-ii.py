# @before-stub-for-debug-begin
from python3problem90 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = list()
        nums.sort()

        def dfs(i, subset):
            if i == len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[i])
            dfs(i + 1, subset)
            subset.pop()

            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1

            dfs(i + 1, subset)

        dfs(0, [])
        return res


# @lc code=end
