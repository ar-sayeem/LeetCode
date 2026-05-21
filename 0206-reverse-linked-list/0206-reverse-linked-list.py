# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr, next = None, head, None

        while curr:
            next = curr.next  # save next
            curr.next = prev  # reverse curr

            # update prev & curr
            prev = curr
            curr = next
        return prev


# Time Complexity   : O(N)
# Space Complexity  : O(1)
# by ar-sayeem [May 21, 2026]
