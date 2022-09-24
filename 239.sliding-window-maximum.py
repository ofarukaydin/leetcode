# @before-stub-for-debug-begin
from python3problem239 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

# @lc code=start
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deq = deque([])
        res = []

        left = 0
        right = 0

        while right < len(nums):
            while len(deq) and nums[right] > nums[deq[-1]]:
                deq.pop()
            deq.append(right)

            if left > deq[0]:
                deq.popleft()

            if right + 1 >= k:
                res.append(nums[deq[0]])
                left += 1

            right += 1

        return res


# @lc code=end
