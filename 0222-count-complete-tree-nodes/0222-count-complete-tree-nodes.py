from typing import Optional

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_height = self.getLeftHeight(root)
        right_height = self.getRightHeight(root)

        # perfect binary tree
        if left_height == right_height:
            return (2**left_height) - 1

        # not a perfect binary tree
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    # dive deep to left
    def getLeftHeight(self, node):
        height = 0
        while node:
            height += 1
            node = node.left
        return height

    # dive deep to right
    def getRightHeight(self, node):
        height = 0
        while node:
            height += 1
            node = node.right
        return height


# Time Complexity   : O(log²N)
# Space Complexity  : O(log N)
# by ar-sayeem [April 30, 2026]
