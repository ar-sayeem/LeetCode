from typing import List

class Solution:
    def createGrid(self, m: int, n: int) -> List[str]:
        return ['.' * n] + ['#' * (n - 1) + '.' for _ in range(m - 1)]

# Time Complexity: O(m * n)
# Space Complexity: O(m * n)
# by ar-sayeem [Oct 17, 2026]