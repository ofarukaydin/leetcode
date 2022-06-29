#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head
        
        i = n
        while right and i > 0:
            right = right.next
            i -= 1
        
        while right:
            right = right.next
            left = left.next

        left.next = left.next.next

        return dummy.next
        



        
# @lc code=end

