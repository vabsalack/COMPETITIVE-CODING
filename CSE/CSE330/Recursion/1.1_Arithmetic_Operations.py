#!/bin/python3

import math
import os
import random
import re
import sys

sys.setrecursionlimit(15000)


#
# Complete the 'arithmeticExpressions' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def arithmeticExpressions(arr):
    n = len(arr)
    operations = [lambda a, b: a + b, lambda a, b: a * b, lambda a, b: a - b]
    operators = ["+", "*", "-"]
    l = [-1] * (n - 1)
    re = ""

    def evaluate(i, value):
        if i == n:
            return True if value % 101 == 0 else None

        for j in range(3):
            if evaluate(i + 1, operations[j](value, arr[i])) is not None:
                l[i - 1] = operators[j]
                return True

    l.append("")
    evaluate(1, arr[0])

    for i in range(n):
        re += f"{arr[i]}{l[i]}"

    return re


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    cache = [{}] * n

    result = arithmeticExpressions(arr)

    fptr.write(result + '\n')

    fptr.close()
