#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashMap = {}

        for num in nums:
            if num in hashMap:
                return True
            hashMap[num] = True
        return False

# @lc code=end
