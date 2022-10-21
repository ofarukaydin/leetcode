# @before-stub-for-debug-begin
from python3problem47 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start
from typing import Counter


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        count = Counter(nums)
        res = []

        def backtrack(perm):
            nonlocal count
            if len(perm) == len(nums):
                res.append(perm.copy())
                return

            for n in count:
                if count[n] > 0:
                    perm.append(n)
                    count[n] -= 1

                    backtrack(perm)

                    perm.pop()
                    count[n] += 1
        backtrack([])
        return res
# @lc code=end
