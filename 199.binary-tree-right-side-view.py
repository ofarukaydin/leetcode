#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        deq = deque()
        deq.append(root)
        res = []

        while deq:
            lastIndex = len(deq) - 1
            for i in range(len(deq)):
                node = deq.popleft()

                if i == lastIndex:
                    res.append(node.val)
                
                if node.left:
                    deq.append(node.left)
                if node.right:
                    deq.append(node.right)
                
        return res
            


# @lc code=end
