from sortedcontainers import SortedList
from collections import defaultdict


class Solution:
    
    def createSortedArray(self, instructions: List[int]) -> int:
        mod = pow(10, 9) + 7
        arr = SortedList()
        dic = defaultdict(int)
        summ = 0
        n = range(len(instructions))

        for i in n:
            # dict frequency count
            cur_ele = instructions[i]
            dic[cur_ele] += 1

            # find the inserstion index to the left,
            # the index is the no of elements to the left
            left = arr.bisect_left(cur_ele)

            # insert element
            arr.add(cur_ele)

            # find the no of elements to the right
            right = len(arr) - left - dic[cur_ele]

            summ = (summ + min(left, right)) % mod

        return summ
