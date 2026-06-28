class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root]
        visit = [False]
        ans = []

        while stack:
            curr, v = stack.pop(), visit.pop()
            if curr:
                if v:
                    ans.append(curr.val)
                else:
                    stack.append(curr)
                    visit.append(True)
                    stack.append(curr.right)
                    visit.append(False)
                    stack.append(curr.left)
                    visit.append(False)

        return ans

# Time Complexity  : O(N)
# Space Complexity : O(H)
# by ar-sayeem [June 28, 2026]
