# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head     # sart from same position

        while fast and fast.next:
            slow = slow.next        # +1 step
            fast = fast.next.next   # +2 step
            if fast == slow:        # will meet if cycle
                return True

        return False                # fast will reach end first, means no cycle


# Time Complexity: O(N)
# Space Complexity: O(1)
# by ar-sayeem [March 15, 2026]
