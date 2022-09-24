# @before-stub-for-debug-begin
from python3problem84 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#

# @lc code=start


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        currMax = 0
        for index, height in enumerate(heights):
            start = index
            while stack and stack[-1][1] > height:
                poppedIndex, poppedHeight = stack.pop()
                currMax = max(poppedHeight, (index - poppedIndex)
                                * poppedHeight, currMax)
                start = poppedIndex

            stack.append((start, height))

        for i, h in stack:
            currMax = max(currMax, h * (len(heights) - i))

        return currMax


# @lc code=end
