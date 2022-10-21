# @before-stub-for-debug-begin
from python3problem42 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start


class Solution:
    def trap(self, height: List[int]) -> int:
        currMaxLeft, currMaxRight = height[0], height[-1]
        left, right = 0, len(height) - 1
        trappedWaters = 0

        while left < right:
            if currMaxLeft <= currMaxRight:
                left += 1
                currMaxLeft = max(currMaxLeft, height[left])
                trappedWaters += currMaxLeft - height[left]
            else:
                right -= 1
                currMaxRight = max(currMaxRight, height[right])
                trappedWaters += currMaxRight - height[right]

        return trappedWaters

# @lc code=end
