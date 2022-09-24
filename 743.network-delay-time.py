# @before-stub-for-debug-begin
from python3problem743 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=743 lang=python3
#
# [743] Network Delay Time
#

# @lc code=start
from collections import defaultdict
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjMap = defaultdict(list)
        minHeap = [(0, k)]
        visited = set()
        res = 0

        for u, v, w in times:
            adjMap[u].append((w, v))

        while minHeap:
            cost, v = heapq.heappop(minHeap)
            if v not in visited:
                res = cost
                visited.add(v)

                for w, nei in adjMap[v]:
                    heapq.heappush(minHeap, (cost + w, nei))

        return res if len(visited) >= n else -1


# @lc code=end
