"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution:
    def flatten(self, head: "Optional[Node]") -> "Optional[Node]":
        curr = head

        while curr:
            if curr.child:
                child = curr.child
                next_node = curr.next  # save next

                tail = child
                while tail.next:
                    tail = tail.next

                # attach child and parent
                curr.next = child
                child.prev = curr

                # attach afterwards (next)
                tail.next = next_node
                if next_node:
                    next_node.prev = tail

                curr.child = None

            curr = curr.next

        return head


# Time Complexity   : O(N)
# Space Complexity  : O(1)
# by ar-sayeem [May 26, 2026]