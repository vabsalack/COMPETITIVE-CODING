class Solution:

    def partition(self, arr, l, r):
        down = l - 1
        pivot = arr[r]

        for i in range(l, r + 1):
            if arr[i] <= pivot:
                down += 1
                arr[i], arr[down] = arr[down], arr[i]

        return down

    def quicksort(self, arr, l, r):

        if l < r:
            parti = self.partition(arr, l, r)
            self.quicksort(arr, l, parti - 1)
            self.quicksort(arr, parti + 1, r)

    def mergesort(self, arr):

        if len(arr) > 1:
            m = len(arr) // 2
            l = arr[:m]
            r = arr[m:]

            self.mergesort(l)
            self.mergesort(r)

            i = j = k = 0

            while i < len(l) and j < len(r):
                if l[i] < r[j]:
                    arr[k] = l[i]
                    i += 1
                else:
                    arr[k] = r[j]
                    j += 1
                k += 1

            while i < len(l):
                arr[k] = l[i]
                i += 1
                k += 1

            while j < len(r):
                arr[k] = r[j]
                j += 1
                k += 1

    def sortArray(self, nums: List[int]) -> List[int]:

        # self.quicksort(nums, 0, len(nums)-1)
        self.mergesort(nums)
        return nums
