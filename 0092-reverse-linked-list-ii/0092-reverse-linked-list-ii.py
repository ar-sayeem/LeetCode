from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
            
        dummy = ListNode(0, head)

        # reach the node before left
        leftPrev = dummy
        curr = head
        for _ in range(left - 1):
            leftPrev = curr
            curr = curr.next

        # reverse portion
        prev = None
        for _ in range(right - left + 1):
            tempNext = curr.next     # save next node
            curr.next = prev
            prev = curr
            curr = tempNext

        # update links
        leftPrev.next.next = curr
        leftPrev.next = prev

        return dummy.next


# Time Complexity   : O(N)
# Space Complexity  : O(1)
# by ar-sayeem [May 29, 2026]