#
# @lc app=leetcode id=1046 lang=python3
#
# [1046] Last Stone Weight
#

# @lc code=start
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) >= 2:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            heapq.heappush(stones, first - second)

        return -stones[0]

# @lc code=end
