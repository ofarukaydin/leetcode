# @before-stub-for-debug-begin
from python3problem11 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start


class Solution:
    def maxArea(self, height: List[int]) -> int:
        currMax = 0
        left, right = 0, len(height) - 1

        while left < right:
            currArea = min(height[left], height[right]) * \
                (right - left)
            currMax = max(currMax, currArea)
            if height[left] < height[right]:
                left += 1
            elif height[right] <= height[left]:
                right -= 1
        return currMax

# @lc code=end
