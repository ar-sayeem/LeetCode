class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        # number of rows and columns in mat
        r, c = len(mat), len(mat[0])
        k %= c  # reduce k according to column size (not row size!)

        # traverse each cell
        for row in range(r):
            for col in range(c):
                # if not same element after k steps (wrap around using c, not col!)
                if mat[row][col] != mat[row][(col + k) % c]:
                    return False
        return True


# Time Complexity: O(r x c)
# Space Complexity: O(1)
# by ar-sayeem [March 27, 2026]
