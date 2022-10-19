#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'equal' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def equal(arr):
    """ finding minimum no of operations to make all values no of choco equal.
        one way - add values to all elements except one = operation count +1
        second way - sub values from each element = operation count +1
        instead of adding values to elements, subtract from them to equal the stack
        try subtracting all to min value of array, to min - 4,
        min - 5, hits the same again.
        """
    ways = [0]*5
    mini = min(arr)

    for i in range(5):
        for j in range(len(arr)):
            temp = arr[i] - mini
            steps = (temp // 5) + ((temp % 5) // 2) + ((temp % 5) % 2)
            ways[i] += steps

        mini -= 1

    return min(ways)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = equal(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
