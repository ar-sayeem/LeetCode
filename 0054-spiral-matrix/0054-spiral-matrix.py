from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        srow, erow = 0, len(matrix) - 1
        scol, ecol = 0, len(matrix[0]) - 1
        ans = []

        while srow <= erow and scol <= ecol:

            # TOP: traverse right
            for j in range(scol, ecol + 1):
                ans.append(matrix[srow][j])

            # RIGHT: traverse down
            for i in range(srow + 1, erow + 1):
                ans.append(matrix[i][ecol])

            # BOTTOM: traverse left
            for j in range(ecol - 1, scol - 1, -1):
                if srow == erow:  # single row left, TOP already collected it
                    break
                ans.append(matrix[erow][j])

            # LEFT: traverse up
            for i in range(erow - 1, srow, -1):
                if scol == ecol:  # single col left, RIGHT already collected it
                    break
                ans.append(matrix[i][scol])

            srow += 1
            erow -= 1
            scol += 1
            ecol -= 1

        return ans


# Time Complexity: O(M x N)
# Space Complexity: O(1)
# by ar-sayeem [March 23, 2026]
