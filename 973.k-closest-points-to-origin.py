#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#

# @lc code=start
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = list(
            map(lambda point: ((point[0] ** 2) + (point[1] ** 2), point), points))

        heapq.heapify(distance)

        res = []

        for _ in range(k):
            res.append(heapq.heappop(distance)[1])

        return res


# @lc code=end
