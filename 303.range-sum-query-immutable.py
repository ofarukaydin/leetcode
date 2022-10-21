#
# @lc app=leetcode id=303 lang=python3
#
# [303] Range Sum Query - Immutable
#

# @lc code=start
class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixSum = []
        currSum = 0
        for num in nums:
            currSum += num
            self.prefixSum.append(currSum)

    def sumRange(self, left: int, right: int) -> int:
        preRight = self.prefixSum[right]
        preLeft = self.prefixSum[left - 1] if left > 0 else 0

        return preRight - preLeft


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# @lc code=end
