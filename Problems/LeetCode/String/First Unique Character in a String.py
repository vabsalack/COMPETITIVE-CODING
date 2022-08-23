class Solution:
    """https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/881/"""
    def dictt(self, s):
        d = dict()
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = 0
            d[s[i]] += 1
        return d

    def firstUniqChar(self, s: str) -> int:
        di = self.dictt(s)
        for i in range(len(s)):
            if di[s[i]] == 1:
                return i
        return -1