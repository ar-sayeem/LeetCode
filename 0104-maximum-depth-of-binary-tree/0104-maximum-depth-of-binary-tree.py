# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        # Approch 1: DFS – Recursive
        if not root:    # NULL tree
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        # If not NULL then at leat 1, then recursive for child cases
    
# Time Complexity: O(n)
# Space Complexity: O(n)