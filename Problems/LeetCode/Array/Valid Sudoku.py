class Solution:
    """https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/769/"""
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = collections.defaultdict(set)
        columns = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):

            for c in range(9):

                value = board[r][c]
                if value == ".":
                    continue
                elif (value in rows[r]) or (value in columns[c]) or (value in squares[(r // 3, c // 3)]):
                    return False

                rows[r].add(value)
                columns[c].add(value)
                squares[(r // 3, c // 3)].add(value)

        return True