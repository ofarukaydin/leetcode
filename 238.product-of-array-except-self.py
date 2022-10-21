#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1 for _ in nums]
        currProduct = 1

        for index, num in enumerate(nums):
            res[index] = currProduct
            currProduct *= num

        currProduct = 1

        for index in range(len(nums) - 1, -1, -1):
            res[index] *= currProduct
            currProduct *= nums[index]

        return res

# @lc code=end
