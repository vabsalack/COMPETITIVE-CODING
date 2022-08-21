class Solution:
    """https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/549/"""
    def singleNumber(self, nums: List[int]) -> int:
        x = 0
        for i in range(len(nums)):
            x ^= nums[i]
        return x