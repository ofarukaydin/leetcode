# @before-stub-for-debug-begin
from python3problem543 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def __init__(self):
        self.currMax = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)

    def dfs(self, node):
        if not node:
            return -1

        left = self.dfs(node.left)
        right = +self.dfs(node.right)

        self.currMax = max(self.currMax, 2 + left + right)

        return 1 + max(left, right)


# @lc code=end
