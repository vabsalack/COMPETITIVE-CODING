class Solution:
    """https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/880/"""
    def reverse_integer(self, n):

        flag = False
        if n < 0:
            n = abs(n)
            flag = True
        rev = 0
        while n:
            rev *= 10
            temp = n % 10
            n = n // 10
            rev += temp

        if flag:
            rev = -1 * rev
            if rev < (-1 * (2 ** 31)):
                return 0
            return rev
        else:
            if rev > (2 ** 31 - 1):
                return 0
            return rev

    def reverse(self, x: int) -> int:
        return self.reverse_integer(x)