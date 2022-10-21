# @before-stub-for-debug-begin
from collections import defaultdict
from python3problem560 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = defaultdict(int)
        prefixSum[0] = 1
        currSum = 0
        res = 0

        for num in nums:
            currSum += num
            res += prefixSum[currSum - k]
            prefixSum[currSum] += 1

        return res


# @lc code=end
