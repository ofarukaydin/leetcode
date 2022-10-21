#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#

# @lc code=start
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = [((x ** 2) + (y ** 2), x, y) for x, y in points]
        heapq.heapify(minHeap)

        res = []
        for _ in range(k):
            dist, x, y = heapq.heappop(minHeap)
            res.append([x, y])

        return res

# @lc code=end
