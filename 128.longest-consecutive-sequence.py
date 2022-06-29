#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        currentLongest = 0
        numSet = set(nums)
        for num in nums:
            # Does not have a left neighbor, so its a starting sequence
            if num - 1 not in numSet:
                longestConsecutiveLen = 1
                while num + longestConsecutiveLen in numSet:
                    longestConsecutiveLen += 1
                currentLongest = max(currentLongest, longestConsecutiveLen)
        return currentLongest


# @lc code=end
