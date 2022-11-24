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

    '''public int findUnsortedSubarray(int[] A) {
    int n = A.length, beg = -1, end = -2, min = A[n-1], max = A[0];
    for (int i=1;i<n;i++) {
      max = Math.max(max, A[i]);
      min = Math.min(min, A[n-1-i]);
      if (A[i] < max) end = i;
      if (A[n-1-i] > min) beg = n-1-i; 
    }
    return end - beg + 1;
}'''