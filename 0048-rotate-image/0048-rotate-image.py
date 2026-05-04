from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):  # Only upper triangle
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                # Swap element at (i,j) with (j,i)

        # Reverse each row
        for row in matrix:
            row.reverse()  # reverse in-place


# Time Complexity   : O(n²)
# Space Complexity  : O(1)
# by ar-sayeem [May 04, 2026]
