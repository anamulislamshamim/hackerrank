#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER maxSum
#  2. INTEGER_ARRAY a
#  3. INTEGER_ARRAY b
#

def twoStacks(maxSum, a, b):
    # Write your code here
    mc = i = j = total = 0
    while i < len(a) and total + a[i] <= maxSum:
        # print(f"mc: {mc}, i: {i}, j: {j}, total: {total}, a[{i}]: {a[i]}")
        total += a[i]
        i += 1
        mc += 1
    
    while j < len(b) and i >= 0:
        # print(f"mc: {mc}, i: {i}, j: {j}, total: {total}, a[{i}]: {a[i]}, b[{j}]: {b[j]}")
        total += b[j]
        j += 1
        
        while i > 0 and total > maxSum:
            i -= 1
            total -= a[i]
        
        if total <= maxSum and mc < i+j:
            mc = i + j
    return mc

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        maxSum = int(first_multiple_input[2])

        a = list(map(int, input().rstrip().split()))

        b = list(map(int, input().rstrip().split()))

        result = twoStacks(maxSum, a, b)

        fptr.write(str(result) + '\n')

    fptr.close()