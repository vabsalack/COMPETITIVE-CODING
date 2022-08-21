class Solution:
    """https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/727/"""
    def removeDuplicates(self, nums: List[int]) -> int:
        i,j = 0,0
        f = i
        n = len(nums)
        while i < n:
            j = i + 1
            while j < n:
                if nums[j] == nums[i]:
                    j += 1
                else:
                    break
            nums[f] = nums[i]
            i = j
            f += 1
        return f