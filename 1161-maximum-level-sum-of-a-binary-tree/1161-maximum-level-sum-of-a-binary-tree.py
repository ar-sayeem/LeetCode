from typing import Optional, List

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level_sums: List[int] = []

        def dfs(node: Optional["TreeNode"], level: int) -> None:
            if node is None:
                return

            if level == len(level_sums):
                level_sums.append(node.val)
            else:
                level_sums[level] += node.val

            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)

        max_sum = max(level_sums)
        return level_sums.index(max_sum) + 1

# Time Complexity: O(N)
# Space Complexity: O(H)
# by ar-sayeem [July 10, 2026]
