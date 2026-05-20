from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next        # 1 step
            fast = fast.next.next   # 2 steps
        return slow                 # slow = middle

# Time Complexity  : O(n)
# Space Complexity : O(1)
# by ar-sayeem [May 20, 2026]