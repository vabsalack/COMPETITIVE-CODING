from sortedcontainers import SortedList


class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)

        pos_ix = {nums2[i]: i for i in range(n)}
        index_val = [pos_ix[nums1[i]] for i in range(n)]

        prefix, sortedlist1 = [], SortedList()
        for i in range(n):
            insert = sortedlist1.bisect_left(index_val[i])
            prefix.append(insert)
            sortedlist1.add(index_val[i])

        suffix, sortedlist2 = [], SortedList()
        for i in range(n - 1, -1, -1):
            insert = sortedlist2.bisect_left(index_val[i])
            suffix.append(len(suffix) - insert)
            sortedlist2.add(index_val[i])

        count = 0
        for i in range(n):
            count += (prefix[i] * suffix[n - 1 - i])

        return count