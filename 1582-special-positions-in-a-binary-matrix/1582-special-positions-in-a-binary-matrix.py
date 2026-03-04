class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        row = len(mat)
        col = len(mat[0])

        row_count = [0] * row  # stores count of 1s in each row
        col_count = [0] * col  # stores count of 1s in each column

        # count 1s in rows and cols
        for i in range(row):
            for j in range(col):
                if mat[i][j] == 1:
                    row_count[i] += 1
                    col_count[j] += 1

        special = 0
        for i in range(row):
            for j in range(col):
                if mat[i][j] == 1 and row_count[i] == 1 and col_count[j] == 1:
                    special += 1

        return special


# Time Complexity: O(Row X Col)
# Space Complexity: O(Row + Col)
# by ar-sayeem [March 04, 2026]
