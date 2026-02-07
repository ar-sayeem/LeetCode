# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:    
  
# Approch 1: DFS – Recursive
        if not root:    # NULL tree
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        # If not NULL then at leat 1, then recursive for child cases
    
# Time Complexity: O(n)
# Space Complexity: O(n)
# by ar-sayeem [February 7, 2026]

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
"""
# Approch 3: Iterative DFS (Pre-order)
        # If the tree is empty, depth is 0
        if not root:
            return 0
        
        # Stack will store (node, current_depth)
        stack = [(root, 1)]
        
        # Variable to track maximum depth found
        res = 0

        # Continue while there are nodes to process
        while stack:
            # Get the top node and its depth
            node, depth = stack.pop()
            
            # Update maximum depth if needed
            res = max(res, depth)
            
            # Push left child with increased depth
            if node.left:
                stack.append((node.left, depth + 1))
            
            # Push right child with increased depth
            if node.right:
                stack.append((node.right, depth + 1))
        
        # Final maximum depth of the tree
        return res

# Time Complexity: O(n) || Space Complexity: O(n)
"""
