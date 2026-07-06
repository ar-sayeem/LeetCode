class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        root_hashes = set()

        def hash_node(node):
            if not node:
                return None
            left_h = hash_node(node.left)
            right_h = hash_node(node.right)
            node_hash = hash((node.val, left_h, right_h))
            root_hashes.add(node_hash)
            return node_hash

        hash_node(root)

        def hash_sub(node):
            if not node:
                return None
            left_h = hash_sub(node.left)
            right_h = hash_sub(node.right)
            return hash((node.val, left_h, right_h))

        return hash_sub(subRoot) in root_hashes

# Time Complexity   : O(N)
# Space Complexity  : O(N)
# by ar-sayeem [July 06, 2026]