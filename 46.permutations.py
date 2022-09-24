# @before-stub-for-debug-begin
from python3problem46 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums, [], res)

        return res

    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
            return

        for i in range(len(nums)):
            self.dfs(nums[0:i] + nums[i+1:], path+[nums[i]], res)


# @lc code=end
