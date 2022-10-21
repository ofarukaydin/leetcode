# @before-stub-for-debug-begin
import heapq
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#

# @lc code=start


class MedianFinder:
    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num: int) -> None:
        self.pushToMaxHeap(num)

        # swap values if needed
        if (
                self.minHeap and
                self.maxHeap and
                self.peekMaxHeap() > self.peekMinHeap()
        ):
            val = self.popMaxHeap()
            self.pushToMinHeap(val)

        # Handle uneven size
        if len(self.minHeap) > len(self.maxHeap) + 1:
            val = self.popMinHeap()
            self.pushToMaxHeap(val)

        if len(self.maxHeap) > len(self.minHeap) + 1:
            val = self.popMaxHeap()
            self.pushToMinHeap(val)

    def findMedian(self) -> float:
        if len(self.maxHeap) == len(self.minHeap):
            return (self.peekMinHeap() + self.peekMaxHeap()) / 2

        elif len(self.minHeap) > len(self.maxHeap):
            return self.peekMinHeap()

        else:
            return self.peekMaxHeap()

    def pushToMaxHeap(self, val):
        heapq.heappush(self.maxHeap, -val)

    def pushToMinHeap(self, val):
        heapq.heappush(self.minHeap, val)

    def peekMinHeap(self):
        return self.minHeap[0]

    def peekMaxHeap(self):
        return -1 * self.maxHeap[0]

    def popMaxHeap(self):
        return -1 * heapq.heappop(self.maxHeap)

    def popMinHeap(self):
        return heapq.heappop(self.minHeap)


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end
