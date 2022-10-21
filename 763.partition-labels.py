# @before-stub-for-debug-begin
from python3problem763 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=763 lang=python3
#
# [763] Partition Labels
#

# @lc code=start


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        positionMap = {}
        res = []

        for i, v in enumerate(s):
            positionMap[v] = i

        goal = 0
        currSize = 0

        for i, v in enumerate(s):
            goal = max(goal, positionMap[v])
            currSize += 1

            if i == goal:
                res.append(currSize)
                currSize = 0

        return res


# @lc code=end
