# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:  # both tree are NULL
            return True
        if not p or not q:  # one of the tree is not NULL
            return False
        if p.val != q.val:  # value not same
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        # check left and right subtrees


# Time Complexity: O(n)
# Space Complexity: O(n)
# by ar-sayeem [February 4, 2026]


# Time Complexity: O(n) -> O(n + m)
# n = number of nodes in tree p
# m = number of nodes in tree q

# Space Complexity: O(n) -> O(max(h_p, h_q))
# h_p = height of tree p
# h_q = height of tree q