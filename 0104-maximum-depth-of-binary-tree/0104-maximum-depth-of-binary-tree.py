# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

# Approch 3: Iterative DFS (Pre-order)
        if not root:
            return 0
        
        stack = [[root, 1]]
        res = 0

        while stack:
            node, depth = stack.pop()
            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return res

# Time Complexity: O(n) || Space Complexity: O(n)
        
"""      
# Approch 1: DFS – Recursive
        if not root:    # NULL tree
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        # If not NULL then at leat 1, then recursive for child cases
    
# Time Complexity: O(n) || Space Complexity: O(n)
"""
"""
# Approch 2: BFS (level-order traversal)
        if not root:
            return 0
        
        level = 0
        q = deque([root])
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level
        
# Time Complexity: O(n) || Space Complexity: O(n)
"""

