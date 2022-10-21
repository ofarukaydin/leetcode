#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, currentSum, path):
            if currentSum == target:
                res.append(path.copy())
                return
            if i == len(candidates) or currentSum > target:
                return

            path.append(candidates[i])
            dfs(i, currentSum + candidates[i], path)

            path.pop()
            dfs(i + 1, currentSum, path)

        dfs(0, 0, [])
        return res
        # @lc code=end
