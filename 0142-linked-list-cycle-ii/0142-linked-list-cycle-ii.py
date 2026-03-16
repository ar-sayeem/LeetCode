# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next            # +1 step
            fast = fast.next.next       # + 2 step

            if slow == fast:            # cycle exsist
                slow = head             # restart slow from head
                while slow != fast:
                    slow = slow.next    # +1 step
                    fast = fast.next    # +1 step
                return slow             # meeting point = cycle start
        
        return None                     # no cycle


# Time Complexity: O(N)
# Space Complexity: O(1)
# by ar-sayeem [March 16, 2026]
