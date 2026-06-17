class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        curr, stack = root, []
        ans = []

        while curr or stack:
            if curr:
                ans.append(curr.val)
                stack.append(curr.right)
                curr = curr.left
            else:
                curr = stack.pop()
        return ans

# Time Complexity  : O(N)
# Space Complexity : O(N)
# by ar-sayeem [June 17, 2026]