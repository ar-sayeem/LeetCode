"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        CopyDict = {None : None}

        curr = head
        while curr:
            copy = Node(curr.val)
            CopyDict[curr] =  copy
            curr = curr.next

        curr = head
        while curr:
            copy = CopyDict[curr]
            copy.next = CopyDict[curr.next]
            copy.random = CopyDict[curr.random]
            curr = curr.next

        return CopyDict[head]


# Time Complexity   : O(N)
# Space Complexity  : O(N)
# by ar-sayeem [May 28, 2026]