# @before-stub-for-debug-begin
from python3problem621 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=621 lang=python3
#
# [621] Task Scheduler
#

# @lc code=start
from collections import deque
import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        deq = deque()  # pairs of [-cnt, idleTime]
        time = 0

        while deq or maxHeap:

            if maxHeap:
                task = heapq.heappop(maxHeap)
                cnt = 1 + task

                if cnt:
                    # push it back to heap at time - 1
                    # so it can be used again
                    deq.append([cnt, time - 1 + n])

            if deq and deq[0][1] == time - 1:
                # push it back to heap just before it becomes
                # available to schedule
                task = deq.popleft()[0]
                heapq.heappush(maxHeap, task)

            time += 1

        return time


# @lc code=end
