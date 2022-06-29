# @before-stub-for-debug-begin
from python3problem347 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurances = defaultdict(int)
        for num in nums:
            occurances[num] += 1

        freqArray = [[] for _ in range(len(nums) + 1)]
        for key, value in occurances.items():
            freqArray[value].append(key)

        result = []
        for occuredItems in reversed(freqArray):
            for value in occuredItems:
                result.append(value)
                if len(result) == k:
                    return result


# @lc code=end
