"""https://leetcode.com/problems/n-queens/"""


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posdia = set()
        negdia = set()

        result = []
        board = [["."] * n for _ in range(n)]

        def btrack(r):
            if r == n:
                result.append(["".join(row) for row in board])
                return
            for c in range(n):
                if c in col or (r + c) in posdia or (r - c) in negdia:
                    continue

                col.add(c)
                posdia.add(r + c)
                negdia.add(r - c)
                board[r][c] = "Q"

                btrack(r + 1)

                col.remove(c)
                posdia.remove(r + c)
                negdia.remove(r - c)
                board[r][c] = "."

        btrack(0)
        return result