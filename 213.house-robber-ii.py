#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[:-1]), self.helper(nums[1:]))

    def helper(self, nums):
        robNextPlusOne = 0
        robNext = 0

        for num in nums:
            current = max(robNext, robNextPlusOne + num)

            robNextPlusOne = robNext
            robNext = current

        return robNext

# @lc code=end
