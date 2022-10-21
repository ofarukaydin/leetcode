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
        N = len(points)
        adjMap = defaultdict(list)

        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                cost = abs(x1 - x2) + abs(y1 - y2)
                adjMap[i].append((cost, j))
                adjMap[j].append((cost, i))

        visited = set()
        minHeap = [(0, 0)]  # (cost, node)

        res = 0
        while len(visited) < N:
            cost, node = heapq.heappop(minHeap)

            if node in visited:
                continue

            visited.add(node)
            res += cost
            for neiCost, neiNode in adjMap[node]:
                if neiNode not in visited:
                    heapq.heappush(minHeap, (neiCost, neiNode))

        return res


# @lc code=end
