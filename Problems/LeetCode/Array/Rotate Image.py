class Solution:
    """https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/770/"""
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead
        """
        l, r = 0, len(matrix) - 1

        while l < r:

            t, b = l, r

            for i in range(r - l):
                topleft = matrix[t][l + i]
                matrix[t][l + i] = matrix[b - i][l]
                matrix[b - i][l] = matrix[b][r - i]
                matrix[b][r - i] = matrix[t + i][r]
                matrix[t + i][r] = topleft

            l += 1
            r -= 1