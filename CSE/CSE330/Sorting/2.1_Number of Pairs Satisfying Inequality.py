from sortedcontainers import SortedList


class Solution:
    # nums1[i] - nums2[j] <= nums2[i] - nums2[j] + diff
    # nums1[i] - nums2[i] <= nums1[j] - nums2[j] + diff

    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        n = len(nums2)

        slist = SortedList()
        count = 0

        # pointer loop
        for i in range(n):
            pointer_sum = nums1[i] - nums2[i] + diff
            insert = slist.bisect_right(pointer_sum)
            slist.add(pointer_sum - diff)

            count += insert

        return count
