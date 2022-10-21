#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i, path):
            if i == len(nums):
                res.append(path.copy())
                return

            path.append(nums[i])
            dfs(i + 1, path)  # include the number

            path.pop()
            dfs(i + 1, path)  # don't include the number

        dfs(0, [])
        return res
# @lc code=end
