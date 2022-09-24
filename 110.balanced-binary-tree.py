#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced, _ = self.dfs(root)

        return balanced

    def dfs(self, root):
        if not root:
            return [True, 0]

        isLeftBalanced, leftHeight = self.dfs(root.left)
        isRightBalanced, rightHeight = self.dfs(root.right)

        balanced = isLeftBalanced and isRightBalanced and abs(
            leftHeight - rightHeight) <= 1
        height = 1 + max(leftHeight, rightHeight)

        return [balanced, height]

# @lc code=end
