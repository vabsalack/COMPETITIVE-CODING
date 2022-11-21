class Solution:
    def mergesort(self, arr):
        if len(arr) <= 1: return 0
        # split half
        m = len(arr) // 2
        l = arr[:m]
        r = arr[m:]

        # recursive call
        count = self.mergesort(l) + self.mergesort(r)

        lenl, lenr = len(l), len(r)
        # businss logic
        startindex = endindex = 0

        for i in range(lenl):
            while startindex < lenr and r[startindex] - l[i] < self.lower:
                startindex += 1
            while endindex < lenr and r[endindex] - l[i] <= self.upper:
                endindex += 1

            count += (endindex - startindex)

        # merge
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

    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:

        self.lower = lower
        self.upper = upper

        n = len(nums)
        prefixsum = [0] * (n + 1)

        for i in range(n):
            prefixsum[i + 1] = (nums[i] + prefixsum[i])

        re = self.mergesort(prefixsum)

        return re
##################################################################################
#solution 2

    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:

        cumsum = [0]
        for n in nums:
            cumsum.append(cumsum[-1] + n)

        # inclusive
        def mergesort(l, r):
            if l == r:
                return 0
            mid = (l + r) // 2
            cnt = mergesort(l, mid) + mergesort(mid + 1, r)

            i = j = mid + 1
            # O(n)
            for left in cumsum[l:mid + 1]:
                while i <= r and cumsum[i] - left < lower:
                    i += 1
                while j <= r and cumsum[j] - left <= upper:
                    j += 1
                cnt += j - i

            cumsum[l:r + 1] = sorted(cumsum[l:r + 1])
            return cnt

        return mergesort(0, len(cumsum) - 1)

#############################################################################


