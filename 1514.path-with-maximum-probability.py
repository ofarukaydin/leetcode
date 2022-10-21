#
# @lc app=leetcode id=1514 lang=python3
#
# [1514] Path with Maximum Probability
#

# @lc code=start
from collections import defaultdict
import heapq


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        adjMap = defaultdict(list)

        for index, (src, dst) in enumerate(edges):
            adjMap[src].append((dst, succProb[index]))
            adjMap[dst].append((src, succProb[index]))

        minHeap = [(-1, start)]  # (prob, node)
        visited = set()

        while minHeap:
            prob, node = heapq.heappop(minHeap)
            if node == end:
                return -prob

            visited.add(node)
            for nei, neiProb in adjMap[node]:
                if nei not in visited:
                    heapq.heappush(minHeap, (prob * neiProb, nei))

        return 0


# @lc code=end
