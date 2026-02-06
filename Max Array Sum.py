#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    
    prev2 = 0 
    prev1 = 0
    
    for i in range(len(arr)):
        aux = prev1
        prev1 = max(prev2+arr[i], prev1)
        prev2 = aux
    return prev1
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
