class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        curr = root
        ans = []

        while curr:
            if not curr.left:
                ans.append(curr.val)
                curr = curr.right
            else:
                predecessor = curr.left
                while predecessor.right and predecessor.right != curr:
                    predecessor = predecessor.right

                if not predecessor.right:
                    ans.append(curr.val)
                    predecessor.right = curr
                    curr = curr.left
                else:
                    predecessor.right = None
                    curr = curr.right
        
        return ans

# Morris Traversal algorithm
# Time Complexity   : O(N)
# Space Complexity  : O(1)
# by ar-sayeem [April 22, 2026]