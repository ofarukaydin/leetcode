#
# @lc app=leetcode id=2130 lang=python3
#
# [2130] Maximum Twin Sum of a Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head.next
        cache = {}
        slowIndex, fastIndex = 0, 1

        while fast and fast.next:
            cache[slowIndex] = slow.val
            cache[fastIndex] = fast.val

            slow = slow.next
            fast = fast.next.next

            slowIndex += 1
            fastIndex += 2

        length = (slowIndex + 1) * 2

        if slow:
            cache[slowIndex] = slow.val
            slow = slow.next
            slowIndex += 1
            cache[slowIndex] = slow.val

        currMax = float('-inf')
        while slow:
            twinIndex = length - 1 - slowIndex
            currMax = max(currMax, cache[twinIndex] + slow.val)
            slow = slow.next
            slowIndex += 1

        return currMax

# @lc code=end
