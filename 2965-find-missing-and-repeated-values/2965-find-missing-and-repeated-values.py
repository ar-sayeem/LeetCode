class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        seen = [False] * (n * n + 1)
        duplicate = -1
        
        for row in grid:
            for num in row:
                if seen[num]:
                    duplicate = num
                else:
                    seen[num] = True
        
        missing = -1
        for i in range(1, n * n + 1):
            if not seen[i]:
                missing = i
                break
        
        return [duplicate, missing]


# Time Complexity: O(n²)
# Space Complexity: O(n²)
# by ar-sayeem [January 17, 2026]