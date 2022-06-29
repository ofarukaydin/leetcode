# @before-stub-for-debug-begin
from python3problem138 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToNewMap = {
            None: None
        }

        cur = head
        while cur:
            oldToNewMap[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur:
            copied = oldToNewMap[cur]
            copied.next = oldToNewMap[cur.next]
            copied.random = oldToNewMap[cur.random]
            cur = cur.next

        return oldToNewMap[head]

        # @lc code=end
