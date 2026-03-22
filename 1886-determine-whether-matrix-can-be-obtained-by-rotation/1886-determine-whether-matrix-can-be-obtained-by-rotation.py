from typing import List

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)  # matrix size

        for _ in range(4):  # 4 rotations (0°, 90°, 180°, 270°)
            if mat == target:  # check if  curr == target matrix
                return True

            # Step 1: Transpose (swap upper triangle only)
            for i in range(n):
                for j in range(i + 1, n):  # j starts from i + 1 to avoid double swap
                    mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

            # Step 2: Reverse each row (completes 90° CW rotation)
            for row in mat:
                row.reverse()

        return False  # no rotation matched


# Time Complexity: O(N²)
# Space Complexity: O(1)
# by ar-sayeem [March 22, 2026]
