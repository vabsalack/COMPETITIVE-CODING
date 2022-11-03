#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'maxSubarray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def maxSubarray(arr):
    # Write your code here
    max_sum = arr[0]
    flag = False
    max_seq = 0
    sum_value = 0

    for i in range(len(arr)):
        """using kadane algo to find subarray max"""
        cur_ele = arr[i]

        sum_value += cur_ele

        max_sum = max(max_sum, sum_value)

        if sum_value < 0:
            sum_value = 0

        ''' max subsequence sum is just sum of positive element. if all element 
        is negative, we take max of list of negative numbers in array '''

        if cur_ele > 0:
            flag = True
            max_seq += cur_ele

    return (max_sum, max_seq) if flag else (max_sum, max(arr))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
