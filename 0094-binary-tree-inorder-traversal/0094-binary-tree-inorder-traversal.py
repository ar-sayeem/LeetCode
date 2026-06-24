class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        stack = []

        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            ans.append(curr.val)
            curr = curr.right

        return ans


        # ans = []

        # def inorder(root):
        #     if not root:
        #         return
        #     inorder(root.left)
        #     ans.append(root.val)
        #     inorder(root.right)

        # inorder(root)
        # return ans

# Time Complexity   : O(N)
# Space Complexity  : O(N)
# by ar-sayeem [June 24, 2026]
