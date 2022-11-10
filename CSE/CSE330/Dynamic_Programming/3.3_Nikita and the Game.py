#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'arraySplitting' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def arraySplitting(arr):
    # Write your code here
    running_sum = 0
    dic = {}

    for i in range(len(arr)):
        running_sum += arr[i]
        dic[running_sum] = i + 1

    if running_sum == 0:
        return len(arr) - 1

    elif running_sum % 2 == 0 and running_sum // 2 in dic:

        split1 = arraySplitting(arr[:dic[running_sum // 2]])
        split2 = arraySplitting(arr[dic[running_sum // 2]:])

        return max(split1, split2) + 1
    else:
        return 0


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        arr_count = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = arraySplitting(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
