class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        end = -1
        maxim = nums[0]

        for i in range(1, n):
            if maxim > nums[i]:
                end = i
            else:
                maxim = nums[i]

        start = 0
        minim = nums[n - 1]

        for i in range(n - 2, -1, -1):
            if minim < nums[i]:
                start = i
            else:
                minim = nums[i]

        return end - start + 1