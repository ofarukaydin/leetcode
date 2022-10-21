# @before-stub-for-debug-begin
from python3problem918 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=918 lang=python3
#
# [918] Maximum Sum Circular Subarray
#

# @lc code=start


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        arraySum = 0

        # global_max_sum denotes the maximum subarray sum without crossing boundary
        # arry_sum - global_min_sum denotes the maximum subarray sum with crossing boundary
        localMinSum, globalMinSum = 0, float('inf')
        localMaxSum, globalMaxSum = 0, float('-inf')

        for num in nums:
            localMinSum = min(num, localMinSum + num)
            localMaxSum = max(num, localMaxSum + num)

            globalMaxSum = max(globalMaxSum, localMaxSum)
            globalMinSum = min(globalMinSum, localMinSum)

            arraySum += num

        # corner case handle for all number are negative
        if globalMaxSum <= 0:
            return globalMaxSum
        else:
            return max(globalMaxSum, arraySum - globalMinSum)


# @lc code=end
