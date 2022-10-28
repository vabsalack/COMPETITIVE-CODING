#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'substrings' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING n as parameter.
#

def substrings(n):
    """ by analyzing the expected output, the substring number forms a pattern,
        eg '5678'
            5 + 50 + 500 + 5000 = 5(1111)
            6 + 60 + 600 = 6(111)
            7  + 70 = 7(11)
            8 = 8(1)"""

    mod = pow(10, 9) + 7

    l = len(n)
    a = [1] * l
    b = [1] * l

    def value(x): return ord(x) - 48

    for i in range(1, l):
        a[i] = (10 * a[i - 1]) % mod
        b[i] = (a[i] + b[i - 1]) % mod
    print(b)

    result = 0
    for i in range(l):
        result += (value(n[i]) * b[l - 1 - i] * (i + 1))
        result %= mod

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = input()

    result = substrings(n)

    fptr.write(str(result) + '\n')

    fptr.close()
