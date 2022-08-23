class Solution:
    """https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/879/"""
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = int(); r = len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1