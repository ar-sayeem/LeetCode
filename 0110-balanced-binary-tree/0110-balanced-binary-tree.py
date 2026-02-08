# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        # Postorder (Left → Right → Node) DFS
        def height(node):
            if not node:
                return 0        # if node empty height = 0
            
            left_height = height(node.left)      # calculate left sub tree
            if left_height == -1:       # -1 means subtree is already imbalance
                return -1       # subtree is unbalanced, early stopping

            right_height = height(node.right)
            if right_height == -1: 
                return -1
            
            if abs(left_height - right_height) > 1:
                return -1       # height difference is more than 1 means NOT BALANCED

            return 1 + max(left_height, right_height)

        return height(root) != -1

# Time Complexity: O(n)
# Space Complexity: O(h) -> worse case O(n) | h = height of tree
# by ar-sayeem [February 8, 2026]