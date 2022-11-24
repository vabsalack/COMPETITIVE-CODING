class Solution:
    def mergesort(self, arr):
        if len(arr) > 1:
            m = len(arr) // 2
            l, r = arr[:m], arr[m:]
            self.mergesort(l)
            self.mergesort(r)

            ll, lr = len(l), len(r)
            i = j = k = 0
            while i < ll and j < lr:
                if l[i] < r[j]:
                    arr[k] = l[i]
                    i += 1
                else:
                    arr[k] = r[j]
                    j += 1
                k += 1

            while i < ll:
                arr[k] = l[i]
                i += 1
                k += 1

            while j < lr:
                arr[k] = r[j]
                j += 1
                k += 1

        return arr

    def findPairs(self, nums: List[int], k: int) -> int:

        n = len(nums)

        self.mergesort(nums)

        # main logic

        i = ans = 0
        j = 1

        while i < n and j < n:

            while 0 < i < j - 1 and nums[i] == nums[i - 1]:
                i += 1

            while j + 1 < n and nums[j] == nums[j + 1]:
                j += 1

            diff = nums[j] - nums[i]

            if diff == k:
                ans += 1
                i += 1
                j += 1

            elif diff < k:
                j += 1

            else:
                i += 1

            if i == j:
                j += 1

        return ans
