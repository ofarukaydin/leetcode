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

        for src, dst, weight in times:
            adjMap[src].append((dst, weight))

        shortestPaths = {}
        minHeap = [(0, k)]  # cost to reach, node

        while minHeap:
            cost, node = heapq.heappop(minHeap)

            if node in shortestPaths:
                continue

            shortestPaths[node] = cost
            for dst, weight in adjMap[node]:
                if dst not in shortestPaths:
                    heapq.heappush(minHeap, (cost + weight, dst))

        return max(shortestPaths.values()) if len(shortestPaths) == n else -1

        # @lc code=end
