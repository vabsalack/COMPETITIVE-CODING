class Solution:
    """https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/578/"""
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = dict()
        for i in range(len(nums)):
            if nums[i] in dic:
                return True
            dic[nums[i]] = 1
        return False