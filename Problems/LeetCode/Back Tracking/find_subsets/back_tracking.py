"""https://leetcode.com/problems/subsets/submissions/"""


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []

        def btrack(i):
            if i == len(nums):
                result.append(subset.copy())
                return

            subset.append(nums[i])
            btrack(i + 1)

            subset.pop()
            btrack(i + 1)

        btrack(0)
        return result