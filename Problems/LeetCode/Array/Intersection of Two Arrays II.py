import collections
""""https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/674/"""

class Solution:
    """this method, first sort the array, and with two pointers, go through you will understand"""

    def method_sort(self, nums1, nums2):
        nums1.sort()
        nums2.sort()

        result = []

        i = j = int()
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums2[j] < nums1[i]:
                j += 1
            else:
                result.append(nums2[j])
                i += 1
                j += 1

        return result

    def method_collection(self, nums1, nums2):
        """ this method use hashmap of nums1 and iterate nums2 to find to intersect and eliminate in hashmap"""
        unique = collections.Counter(nums1)
        result = []
        for ele in nums2:
            if ele in unique:
                unique[ele] -= 1
                result.append(ele)
            if not unique[ele]:
                del unique[ele]
        return result

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        functions = [self.method_collection, self.method_sort]
        return functions[1](nums1, nums2)
