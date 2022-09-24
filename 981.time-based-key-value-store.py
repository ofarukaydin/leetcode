# @before-stub-for-debug-begin
from python3problem981 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=981 lang=python3
#
# [981] Time Based Key-Value Store
#

# @lc code=start
from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.map[key]

        left = 0
        right = len(values) - 1

        res = ''

        while left <= right:
            middle = (left + right) // 2

            valTs = values[middle][0]

            if valTs <= timestamp:
                res = values[middle][1]
                left = middle + 1
            else:
                right = middle - 1

        return res

        # Your TimeMap object will be instantiated and called as such:
        # obj = TimeMap()
        # obj.set(key,value,timestamp)
        # param_2 = obj.get(key,timestamp)
        # @lc code=end
