class Solution:
    """https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/883/"""
    def isPalindrome(self, s: str) -> bool:

        string = ""
        for letter in s:
            if letter.isalnum():
                string += letter.lower()

        if string == "":
            return True

        size = len(string)
        limit = size // 2
        ran = range(0, 1) if limit == 0 else range(0, limit)

        for i in ran:
            if string[i] != string[size - i - 1]:
                return False

        return True