# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ### Morris Inorder Traversal ###
        res = []
        curr = root

        while curr:
            if not curr.left:
                res.append(curr.val)
                curr = curr.right
            else:
                predecessor = curr.left         # predecessor = The rightmost node in curr’s left subtree.
                while predecessor.right and predecessor.right != curr:
                    predecessor = predecessor.right
                
                if not predecessor.right:
                    predecessor.right = curr
                    curr = curr.left
                else:
                    predecessor.right = None
                    res.append(curr.val)
                    curr = curr.right
        return res
  
# Time Complexity: O(n)
# Space Complexity: O(1)
# by ar-sayeem [February , 2026]

        
        # res = []
        # stack = []
        # curr = root

        # while curr or stack:        # if both curr and stack is available
        #     while curr:             # if curr available go left as long as possible
        #         stack.append(curr)
        #         curr = curr.left
        #     curr = stack.pop()      # if there is nothing in left pop, then add it's value to result
        #     res.append(curr.val)
        #     curr = curr.right       # since value is added of left node, time to do same for right nodes
        # return res

# Time Complexity: O(n)
# Space Complexity: O(n)
# by ar-sayeem [February 2, 2026]
