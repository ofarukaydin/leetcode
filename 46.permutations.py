#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(i):
            if i == len(nums):
                return [[]]

            nextPerms = backtrack(i+1)
            resPerms = []

            for perm in nextPerms:
                for j in range(len(perm) + 1):
                    permCopy = perm.copy()
                    permCopy.insert(j, nums[i])
                    resPerms.append(permCopy)

            return resPerms

        return backtrack(0)

# @lc code=end
