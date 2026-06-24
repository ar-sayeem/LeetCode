class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def inorder(root):
            if not root:
                return
            inorder(root.left)
            ans.append(root.val)
            inorder(root.right)

        inorder(root)
        return ans

# Time Complexity   : O(N)
# Space Complexity  : O(N)
# by ar-sayeem [June 24, 2026]
