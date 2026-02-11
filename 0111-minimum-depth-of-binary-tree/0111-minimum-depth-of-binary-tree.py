# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:        # if no nodes depth is 0
            return 0

        queue = deque()     # create a empty queue
        depth = 1
        queue.append((root, depth))     # add root & ini. depth

        while queue:        # if queue not empty we continue
            curr, d = queue.popleft()       # remove first element (FIFO order)

            if curr.left is None and curr.right is None:        # if no child reurn depth / curr level of tree
                return d
            if curr.left:
                queue.append((curr.left, d + 1))
            if curr.right:
                queue.append((curr.right, d + 1))

        return depth        # not really needed (safety return)


# Time Complexity: O(n)
# Space Complexity: O(n)
# by ar-sayeem [February 11, 2026]
