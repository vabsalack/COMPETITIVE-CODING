class Solution:
    def hIndex(self, citations: List[int]) -> int:
        carr = [0] * 5001
        n = len(citations)

        for i in range(n):
            carr[citations[i]] += 1

        for i in range(999, -1, -1):
            carr[i] += carr[i + 1]

        h = 0
        for i in range(n + 1):
            if carr[i] >= i:
                h = max(h, i)

        return h