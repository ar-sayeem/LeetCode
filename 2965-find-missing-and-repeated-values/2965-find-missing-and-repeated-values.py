class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        duplicate = -1
        actual_sum = 0

        for i in range(n):
            for j in range(n):
                current_number = abs(grid[i][j])
                actual_sum += current_number

                position = current_number - 1
                target_row = position // n
                target_col = position % n

                if grid[target_row][target_col] < 0:
                    duplicate = current_number
                else:
                    grid[target_row][target_col] *= -1

        expected_sum = (n * n) * (n * n + 1) // 2

        missing = expected_sum + duplicate - actual_sum
        
        return [duplicate, missing]


# Time Complexity: O(n²)
# Space Complexity: O(1)
# by ar-sayeem [January 17, 2026]