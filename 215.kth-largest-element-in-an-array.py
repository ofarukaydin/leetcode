#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        left, right = 0, len(nums) - 1
        kthIndex = len(nums) - k

        while left < right:
            pivotIndex = self.partition(nums, left, right)

            if pivotIndex < kthIndex:
                left = pivotIndex + 1
            elif pivotIndex > kthIndex:
                right = pivotIndex - 1
            else:
                break

        return nums[kthIndex]

    def partition(self, nums, left, right):
        pivot, fill = nums[right], left

        for i in range(left, right):
            if nums[i] <= pivot:
                nums[fill], nums[i] = nums[i], nums[fill]
                fill += 1

        nums[fill], nums[right] = nums[right], nums[fill]
        return fill


# @lc code=end
