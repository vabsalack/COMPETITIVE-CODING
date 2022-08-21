
class Solution:
    """https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/564/"""
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            diff = prices[i] - prices[i - 1]
            if diff > 0:
                profit += diff
        return profit