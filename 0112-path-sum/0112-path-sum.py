# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, currSum):
            if not node:  # if empty node
                return False

            currSum += node.val  # add values to sum
            if not node.left and not node.right:  # if leaf node check part sum
                return currSum == targetSum  # returns a boolean value

            return dfs(node.left, currSum) or dfs(node.right, currSum)
            # check both subTree

        return dfs(root, 0)  # call dfs and currSum = 0


# Time Complexity: O(N)
# Space Complexity: O(H)
# by ar-sayeem [February 28, 2026]
