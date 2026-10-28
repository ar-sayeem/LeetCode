class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        row = [set() for _ in range(n)]

        for i in range(m):
            for j in range(n):
                v = grid[i][j]
                new = set()
                if i == 0 and j == 0:
                    new.add(v)
                if i > 0:
                    for x in row[j]:
                        new.add(x ^ v)
                if j > 0:
                    for x in row[j - 1]:
                        new.add(x ^ v)
                row[j] = new

        return min(row[n - 1])

# Time Complexity  : O(m * n * 1024)
# Space Complexity : O(n * 1024)
# by ar-sayeem [Oct 28, 2026]