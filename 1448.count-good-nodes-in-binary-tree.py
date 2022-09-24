#
# @lc app=leetcode id=1448 lang=python3
#
# [1448] Count Good Nodes in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def dfs(node, maxVal):
            nonlocal count
            if not node:
                return

            maxVal = max(maxVal, node.val)

            dfs(node.left, maxVal)
            dfs(node.right, maxVal)

            if maxVal == node.val:
                count += 1

        dfs(root, root.val)
        return count
# @lc code=end
