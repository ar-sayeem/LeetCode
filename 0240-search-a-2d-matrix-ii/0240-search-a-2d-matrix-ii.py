from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        rows, cols = len(matrix), len(matrix[0])
        r, c = 0, cols - 1          # start from top-right corner

        while r < rows and c >= 0:
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                c -= 1              # too big, move left
            else:
                r += 1              # too small, move down

        return False

# Time Complexity: O(m + n)
# Space Complexity: O(1)
# by ar-sayeem [March 24, 2026]