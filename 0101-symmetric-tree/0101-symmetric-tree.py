# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(Ltree, Rtree):
            if not Ltree and not Rtree:   # both tree empty
                return True
            if not Ltree or not Rtree:    # one of tree empty
                return False

            return (
                Ltree.val == Rtree.val   # values match
                and dfs(Ltree.left, Rtree.right)
                and dfs(Ltree.right, Rtree.left)
            )

        return dfs(root.left, root.right)  # compare left and right subtrees



# Time Complexity: O(n)
# Space Complexity: O(n)
# by ar-sayeem [February 6, 2026]
