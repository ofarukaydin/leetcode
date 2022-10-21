# @before-stub-for-debug-begin
from python3problem45 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start


class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r, hops = 0, 0, 0

        while r < len(nums) - 1:
            farthest = 0

            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            hops += 1
        return hops


# @lc code=end
