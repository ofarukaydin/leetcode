# @before-stub-for-debug-begin
from python3problem502 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=502 lang=python3
#
# [502] IPO
#
# @lc code=start
import heapq


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        minCapitalHeap = []
        maxProfitHeap = []

        for index, cap in enumerate(capital):
            heapq.heappush(minCapitalHeap, (cap, index))

        availableCapital = w

        for _ in range(k):
            # Projects that can be selected within the available capital. Insert these in a max-heap
            while minCapitalHeap and minCapitalHeap[0][0] <= availableCapital:
                cap, index = heapq.heappop(minCapitalHeap)
                heapq.heappush(maxProfitHeap, (-profits[index], index))

            # Break if we are not able to find any project that can be completed within the available capital
            if not maxProfitHeap:
                break

            availableCapital += -heapq.heappop(maxProfitHeap)[0]

        return availableCapital


# @lc code=end


# @lc code=end
