#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict, deque


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        deq = deque()
        deq.append(root)

        res = defaultdict(list)
        level = 0

        while len(deq) > 0:
            for _ in range(len(deq)):
                node = deq.popleft()
                res[level].append(node.val)

                if node.left:
                    deq.append(node.left)

                if node.right:
                    deq.append(node.right)

            level += 1

        return res.values()


# @lc code=end
