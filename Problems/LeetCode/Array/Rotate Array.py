class Solution:
    """https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/646/"""
    def reverse(self, arr, i, j):
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        r = k % n
        if r:
            self.reverse(nums, 0, n - 1)
            self.reverse(nums, 0, r - 1)
            self.reverse(nums, r, n - 1)

    # def rotate(self, nums: List[int], k: int) -> None:
    #         n = len(nums)
    #         r = k % n
    #         if r:
    #             temp = nums[-r:] + nums[:-r]
    #             for i in range(n):
    #                 nums[i] = temp[i]