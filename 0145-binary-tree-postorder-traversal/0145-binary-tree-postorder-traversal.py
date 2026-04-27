from typing import List

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        stack = []
        curr = root
        prev = None

        while curr or stack:            # stop when empty
            while curr:
                stack.append(curr)      # save node, go left
                curr = curr.left

            curr = stack[-1]            # peek at top

            # no right child, OR already done with right side
            if curr.right is None or curr.right == prev:
                ans.append(curr.val)    # record this node
                prev = curr
                stack.pop()             # remove from stack
                curr = None             # go back up
            else:
                curr = curr.right       # explore right side

        return ans


# Time Complexity   : O(N)
# Space Complexity  : O(H)
# by ar-sayeem [April 27, 2026]
