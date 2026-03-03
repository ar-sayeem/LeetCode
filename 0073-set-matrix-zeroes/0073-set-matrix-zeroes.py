class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row, col = len(matrix), len(matrix[0])

        firstRowZero = False
        firstColZero = False

        # check 1st row
        for j in range(col):
            if matrix[0][j] == 0:
                firstRowZero = True
                break
        
        # check 1st col
        for i in range(row):
            if matrix[i][0] == 0:
                firstColZero = True
                break

        # 1st row and col as marker
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        # set cells to zero based on markers
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        # zero 1st row
        if firstRowZero:
            for j in range(col):
                matrix[0][j] = 0
        # zero 1st col
        if firstColZero:
            for i in range(row):
                matrix[i][0] = 0


# Time Complexity: O(RowXCol)
# Space Complexity: O(1)
# by ar-sayeem [March 03, 2026]