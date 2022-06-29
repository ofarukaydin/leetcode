# @before-stub-for-debug-begin
from python3problem133 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        oldToNewMap = {}

        def dfs(node):
            if node in oldToNewMap:
                return oldToNewMap[node]

            copy = Node(node.val)
            oldToNewMap[node] = copy

            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy

        return dfs(node) if node else None

# @lc code=end
