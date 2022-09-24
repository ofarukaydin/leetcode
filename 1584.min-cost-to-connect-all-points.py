#
# @lc app=leetcode id=1584 lang=python3
#
# [1584] Min Cost to Connect All Points
#

# @lc code=start
from collections import defaultdict
import heapq


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        minheap = [(0, 0)]
        adjMap = defaultdict(list)
        visited = set()
        res = 0

        for i in range(len(points)):
            for j in range(len(points)):
                if i != j:
                    dist = abs(points[i][0] - points[j][0]) + \
                        abs(points[i][1] - points[j][1])
                    adjMap[i].append((dist, j))

        while len(visited) != len(adjMap):
            cost, v = heapq.heappop(minheap)
            if v not in visited:
                visited.add(v)
                res += cost
                for cost, nei in adjMap[v]:
                    heapq.heappush(minheap, (cost, nei))

        return res
        # @lc code=end
