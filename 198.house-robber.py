#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def __init__(self):
        self.dp = []

    def rob(self, nums: List[int]) -> int:
        N = len(nums)

        robNextPlusOne = 0
        robNext = nums[N - 1]

        for i in range(N - 2, -1, -1):
            current = max(robNext, robNextPlusOne + nums[i])
            
            robNextPlusOne = robNext
            robNext = current

        return robNext

        # @lc code=end
