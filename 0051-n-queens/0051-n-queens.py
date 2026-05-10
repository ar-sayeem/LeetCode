class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiag = set()     # (r + c)
        negDiag = set()     # (r - c)

        ans = []
        board = [["."] * n for i in range(n)]

        def backTract(r):
            if r == n:
                copy = ["".join(row) for row in board]
                ans.append(copy)
                return

            for i in range(n):
                if i in col or (r + i) in posDiag or (r - i) in negDiag:
                    continue

                col.add(i)
                posDiag.add(r + i)
                negDiag.add(r - i)
                board[r][i] = "Q"

                backTract(r + 1)

                col.remove(i)
                posDiag.remove(r + i)
                negDiag.remove(r - i)
                board[r][i] = "."

        backTract(0)

        return ans


# Time Complexity   : O(N!)
# Space Complexity  : O(N²)
# by ar-sayeem [May 10, 2026]