from typing import List

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        row, col = len(grid), len(grid[0])

        totalSum = sum(sum(r) for r in grid)

        if totalSum % 2 != 0:       # odd total can never be split equally
            return False

        currSum = 0
        for num in range(row - 1):          # stop before last row
            currSum += sum(grid[num])
            if currSum * 2 == totalSum:     # top half == bottom half
                return True

        currSum = 0
        for j in range(col - 1):        # stop before last col
            for i in range(row):        # sum all rows in this col
                currSum += grid[i][j]
            if currSum * 2 == totalSum:     # left half == right half
                return True
        return False


# Time Complexity: O(M x N)
# Space Complexity: O(1)
# by ar-sayeem [March 25, 2026]
