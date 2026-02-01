#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    i = 0
    jumps = 0
    while i < len(c):
        if i == len(c) - 1:
            return jumps
        elif i + 2 <= len(c)-1 and c[i+2] == 0:
            jumps += 1
            i += 2
        elif i+1 <= len(c)-1 and c[i+1] == 0:
            jumps += 1
            i += 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
