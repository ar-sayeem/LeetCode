class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        k %= m * n

        def pos_to_val(r, c):
            # turn (row, col) into a single flat index
            return r * n + c

        def val_to_pos(v):
            # turn a flat index back into (row, col)
            return v // n, v % n

        res = [[0] * n for _ in range(m)]

        for r in range(m):
            for c in range(n):
                newVal = (pos_to_val(r, c) + k) % (m * n)
                newR, newC = val_to_pos(newVal)
                res[newR][newC] = grid[r][c]

        return res

# Time Complexity   : O(m * n)
# Space Complexity  : O(m * n)
# by ar-sayeem [July 20, 2026]