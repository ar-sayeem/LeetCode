class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head  # Nothing to rotate

        length, tail = 1, head
        while tail.next:  # Length of list
            tail = tail.next
            length += 1

        k = k % length  # Rotation by remainder
        if k == 0:
            return head

        tail.next = head  # Stitch tail to head

        steps = length - k - 1  # New tail distance from original head
        new_tail = head
        for _ in range(steps):
            new_tail = new_tail.next  # Walk to the cut point
        new_head = new_tail.next
        new_tail.next = None  # Snip the circle open

        return new_head


# Time Complexity   : O(N)
# Space Complexity  : O(1)
# by ar-sayeem [May 05, 2026]
