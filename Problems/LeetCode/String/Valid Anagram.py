class Solution:
    """https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/882/"""
    def isAnagram(self, s: str, t: str) -> bool:
        len_s, len_t = len(s), len(t)
        if len_s != len_t:
            return False
        s = [i for i in s]
        t = [i for i in t]
        s.sort()
        t.sort()
        if s == t:
            return True
        return False