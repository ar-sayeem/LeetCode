class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWs, COLs = len(matrix), len(matrix[0])

        # Binary search to find the correct row
        topROW, botROW = 0, ROWs - 1
        while topROW <= botROW:
            row = (topROW + botROW) // 2
            if target > matrix[row][-1]:  # Target is in a lower row
                topROW = row + 1
            elif target < matrix[row][0]:  # Target is in an upper row
                botROW = row - 1
            else:  # Target is in this row
                break
        
        # If no valid row found
        if not (topROW <= botROW):
            return False
        
        # Binary search within the found row
        l, r = 0, COLs - 1
        while l <= r:
            m = (l + r) // 2
            if target < matrix[row][m]:
                r = m - 1
            elif target > matrix[row][m]:
                l = m + 1
            else:  # Target found
                return True
        return False

# Time Complexity: O(log m + log n)
    # m = number of rows
    # n = number of columns
# Space Complexity: O(1)
# by ar-sayeem [February 15, 2026]