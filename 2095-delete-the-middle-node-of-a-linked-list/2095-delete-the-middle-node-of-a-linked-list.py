class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # only 1 node
        if not head.next:
            return None

        slow = head
        fast = head.next.next

        while fast and fast.next:
            slow = slow.next  # +1 step
            fast = fast.next.next  # +2 step

        slow.next = slow.next.next  # skip middle node

        return head

# Time Complexity  : O(N)
# Space Complexity : O(1)
# by ar-sayeem [June 15, 2026]