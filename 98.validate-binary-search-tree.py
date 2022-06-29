#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def valid(node, left, right):
            if not node:
                return True

            if (node.val > left and
                node.val < right and
                valid(node.left, left, node.val) and
                valid(node.right, node.val, right)
                ):
                return True

            return False

        return valid(root, float('-inf'), float('+inf'))


# @lc code=end
