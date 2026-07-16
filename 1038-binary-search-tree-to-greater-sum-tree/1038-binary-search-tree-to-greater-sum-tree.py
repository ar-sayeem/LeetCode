class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.total = 0

        def traverse(node):
            if not node:
                return
            traverse(node.right)
            self.total += node.val

            node.val = self.total
            traverse(node.left)

        traverse(root)
        return root

# Time Complexity   : O(N)
# Space Complexity  : O(H)
# by ar-sayeem [July 16, 2026]