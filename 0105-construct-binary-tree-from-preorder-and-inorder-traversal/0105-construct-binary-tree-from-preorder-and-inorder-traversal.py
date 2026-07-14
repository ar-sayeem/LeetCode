class Solution:
    def buildTree(self, preorder, inorder):
        def search(left, right, val):
            for i in range(left, right + 1):
                if inorder[i] == val:
                    return i
            return -1

        def helper(left, right):
            nonlocal pre_idx
            if left > right:
                return None
            root = TreeNode(preorder[pre_idx])
            in_idx = search(left, right, preorder[pre_idx])
            pre_idx += 1
            root.left = helper(left, in_idx - 1)
            root.right = helper(in_idx + 1, right)
            return root

        pre_idx = 0
        return helper(0, len(inorder) - 1)

# Time Complexity   : O(n²)
# Space Complexity  : O(n)
# by ar-sayeem [July 14, 2026]