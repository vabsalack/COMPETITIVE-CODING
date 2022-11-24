class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        n = len(nums)

        carr = [0] * 201
        for i in range(n):
            carr[nums[i] + 100] += 1

        finarr = [[] for _ in range(101)]

        for i in range(200, -1, -1):
            finarr[carr[i]].append(i - 100)

        res = []
        for freq, ele_arr in enumerate(finarr):
            for ele in ele_arr:
                res.extend([ele] * freq)

        return res