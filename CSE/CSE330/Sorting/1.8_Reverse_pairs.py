class Solution:
    def mergesort(self, arr):
        if len(arr) < 2:
            return 0

        m = len(arr) // 2
        l, r = arr[:m], arr[m:]

        count = self.mergesort(l) + self.mergesort(r)

        lenl, lenr = len(l), len(r)
        i = j = 0

        while i < lenl and j < lenr:
            if l[i] > 2 * r[j]:
                count += (lenl - i)
                j += 1
            else:
                i += 1

        i = j = k = 0

        while i < lenl and j < lenr:
            if l[i] < r[j]:
                arr[k] = l[i]
                i += 1
            else:
                arr[k] = r[j]
                j += 1
            k += 1

        while i < lenl:
            arr[k] = l[i]
            i += 1
            k += 1

        while j < lenr:
            arr[k] = r[j]
            j += 1
            k += 1

        return count

    def reversePairs(self, nums: List[int]) -> int:
        re = self.mergesort(nums)
        return re
