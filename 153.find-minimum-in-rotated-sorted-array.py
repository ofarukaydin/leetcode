# @before-stub-for-debug-begin
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
import math


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        curMin = math.inf



        while left <= right:
            if nums[left] < nums[right]:
                curMin = min(curMin, nums[left])
                break
            mid = (left + right) // 2
            curMin = min(curMin, nums[mid])
            # we're in left sorted portion, we need to go right
            if nums[mid] >= nums[left]:
                left = mid + 1

            else:
                right = mid - 1

        return curMin

# @lc code=end

