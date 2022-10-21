#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = [target - num for num in nums]
        hashMap = {num: i for i, num in enumerate(nums)}

        for i, num in enumerate(diff):
            if num in hashMap and i != hashMap[num]:
                return [i, hashMap[num]]

            # @lc code=end
