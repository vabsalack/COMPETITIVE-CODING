class Solution:
    """https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/546/"""
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            remain = target - nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] == remain:
                    return [i, j]