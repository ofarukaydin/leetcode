# @before-stub-for-debug-begin
from python3problem40 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, subset, target):
            if target == 0:
                res.append(subset.copy())
                return
            elif i >= len(candidates) or target < 0:
                return

            candidate = candidates[i]
            subset.append(candidate)
            dfs(i+1, subset, target - candidate)
            subset.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1

            dfs(i+1, subset, target)

        dfs(0, [], target)
        return res

# @lc code=end
