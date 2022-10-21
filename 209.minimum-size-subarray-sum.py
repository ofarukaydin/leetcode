#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length = float('inf')
        left = 0
        currSum = 0

        for right in range(len(nums)):
            currSum += nums[right]

            while currSum >= target:
                length = min(right - left + 1, length)
                currSum -= nums[left]
                left += 1

        return 0 if length == float('inf') else length

# @lc code=end
