#
# @lc app=leetcode id=724 lang=python3
#
# [724] Find Pivot Index
#

# @lc code=start
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum = 0
        total = sum(nums)

        for index, num in enumerate(nums):
            rightSum = total - leftSum - num
            if rightSum == leftSum:
                return index
            leftSum += num

        return -1


# @lc code=end
