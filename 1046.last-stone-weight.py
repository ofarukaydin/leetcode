#
# @lc app=leetcode id=1046 lang=python3
#
# [1046] Last Stone Weight
#

# @lc code=start
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        newlist = [-weight for weight in stones]
        heapq.heapify(newlist)

        while len(newlist) > 1:
            first = heapq.heappop( newlist)
            second = heapq.heappop(newlist)

            if first != second:
                newWeight = first - second
                heapq.heappush(newlist, newWeight)

        return newlist[0] * - 1 if len(newlist) else 0


# @lc code=end
