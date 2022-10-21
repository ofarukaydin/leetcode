#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets = []

        def dfs(i, path):
            if i == len(nums):
                subsets.append(path.copy())
                return

            # decision to include num
            path.append(nums[i])
            dfs(i+1, path)
            path.pop()

            # decision to not include num
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            dfs(i+1, path)

        dfs(0, [])

        return subsets

# @lc code=end
