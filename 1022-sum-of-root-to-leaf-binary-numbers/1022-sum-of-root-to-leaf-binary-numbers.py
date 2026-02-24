# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(node, curr_val):
            if not node:  # node empty
                return 0

            # left shift by 1 and add curr node's bit
            curr_val = (curr_val << 1) | node.val

            # if leaf node, return curr binary number for this path
            if not node.left and not node.right:
                return curr_val

            # sum of left and right subtree paths
            return dfs(node.left, curr_val) + dfs(node.right, curr_val)

        return dfs(root, 0)  # returns the sum of all root-to-leaf binary numbers


# Time Complexity: O(N)
# Space Complexity: O(H)
# by ar-sayeem [February 24, 2026]
