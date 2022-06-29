# @before-stub-for-debug-begin
from python3problem57 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for index, interval in enumerate(intervals):
            if newInterval[1] < interval[0]:
                res.append(newInterval)
                return res + intervals[index:]
            elif newInterval[0] > interval[1]:
                res.append(interval)
            else:
                newInterval = [min(interval[0], newInterval[0]),
                               max(interval[1], newInterval[1])]
        res.append(newInterval)
        return res


# @lc code=end
