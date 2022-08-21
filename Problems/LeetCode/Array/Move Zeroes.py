class Solution:
    """https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/567/"""
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) != 1:

            j = 0
            for i in range(len(nums)):
                if nums[i] != 0:
                    nums[i], nums[j] = nums[j], nums[i]
                    j += 1
