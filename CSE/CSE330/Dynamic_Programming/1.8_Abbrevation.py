#!/bin/python3

import math
import os
import random
import re
import sys

sys.setrecursionlimit(10000)


#
# Complete the 'abbreviation' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def abbreviation(a, b):
    # Write your code here
    global memo, possible
    memo = set()
    possible = False
    memo.clear()

    def recursion(a, b):
        global memo, possible

        if possible or len(a) < len(b):
            return
        if len(b) == 0:
            if a.islower() or len(a) == 0:
                possible = True
            return

        temp = a + "#" + b
        if temp in memo:
            return
        memo.add(temp)

        fc = a[0:1]
        a = a[1:]
        if fc.islower():
            recursion(a, b)
        if fc.upper() != b[0:1]:
            return
        b = b[1:]
        recursion(a, b)

        return

    recursion(a, b)
    return "YES" if possible else "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        a = input()

        b = input()

        result = abbreviation(a, b)

        fptr.write(result + '\n')

    fptr.close()
