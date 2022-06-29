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
        leftPointer, rightPointer = 0, len(height) - 1
        maxArea = 0
        while leftPointer < rightPointer:
            areaW = rightPointer - leftPointer
            areaH = min(height[leftPointer], height[rightPointer])
            maxArea = max(maxArea, areaH * areaW)
            
            if height[leftPointer] < height[rightPointer]:
                leftPointer += 1
            elif height[rightPointer] < height[leftPointer]:
                rightPointer -= 1
            else:
                leftPointer += 1
        return maxArea
            
            


        
# @lc code=end

