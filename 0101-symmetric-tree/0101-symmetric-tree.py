class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def same(a, b):
            if a == None and b == None:
                return True
            if a == None or b == None:
                return False
            if a.val != b.val:
                return False
            
            return same(a.left, b.right) and same(a.right, b.left)
        
        return same(root.right, root.left)
    
# Time Complexity   : O(N)
# Space Complexity  : O(H)
# by ar-sayeem [July 05, 2026]