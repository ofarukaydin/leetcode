# @before-stub-for-debug-begin
from python3problem105 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        rootIndex = inorder.index(preorder[0])

        root = TreeNode(preorder[0])
        root.left = self.buildTree(
            preorder[1:rootIndex+1], inorder[:rootIndex])
        root.right = self.buildTree(
            preorder[rootIndex+1:], inorder[rootIndex+1:])

        return root

# @lc code=end
