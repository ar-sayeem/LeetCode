from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []

        q = deque([root])
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            level = level[::-1] if len(res) % 2 else level
            res.append(level)

        return res

# Time Complexity   : O(N)
# Space Complexity  : O(N)
# by ar-sayeem [July 29, 2026]