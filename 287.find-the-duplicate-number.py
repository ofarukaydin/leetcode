# @before-stub-for-debug-begin
from python3problem287 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#

# @lc code=start


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if nums[slow] == nums[fast]:
                break

        slow2 = 0
        while slow2 != slow:
            slow = nums[slow]
            slow2 = nums[slow2]


        return slow2


# @lc code=end
