# @before-stub-for-debug-begin
from python3problem739 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []  # pair: [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                _, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((t, i))
        return res


# @lc code=end
