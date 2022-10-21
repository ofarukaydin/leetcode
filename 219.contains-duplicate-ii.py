# @before-stub-for-debug-begin
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#

# @lc code=start


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()  # Cur window of size <= k
        L = 0
        if k == 0:
            return False

        for R in range(len(nums)):
            if nums[R] in window:
                return True
            if R - L + 1 > k:
                window.remove(nums[L])
                L += 1

            window.add(nums[R])

        return False

# @lc code=end
