#!/bin/python3

import math
import os
import random
import re
import sys

sys.setrecursionlimit(10 ** 8)


#
# Complete the 'passwordCracker' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY passwords
#  2. STRING loginAttempt
#

def passwordCracker(passwords, loginAttempt):
    memo = dict()

    # Write your code here

    def match(source, target, i):
        for x, y in zip(source, target[i:]):
            if x != y:
                return False
        else:
            return True

    def recursion(np, pl, i):
        if np == loginAttempt:
            return " ".join(pl)
        if i >= len(loginAttempt):
            return "WRONG PASSWORD"
        for pa in passwords:
            if loginAttempt[i] == pa[0]:
                if match(pa, loginAttempt, i):

                    if np + pa in memo:
                        continue
                    up = np + pa
                    upl = pl + [pa]
                    result = recursion(up, upl, i + len(pa))
                    memo[up] = 1
                    if result != "WRONG PASSWORD":
                        return result
        return "WRONG PASSWORD"

    if set(loginAttempt).intersection(set("".join(passwords))) == set(loginAttempt):
        return recursion("", [], 0)
    else:
        return "WRONG PASSWORD"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        passwords = input().rstrip().split()

        loginAttempt = input()

        result = passwordCracker(passwords, loginAttempt)

        fptr.write(result + '\n')

    fptr.close()
