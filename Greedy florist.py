#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    if k >= len(c):
        return sum(c)
    
    #there are more flowers than people
    c.sort(reverse=True)
    ans = 0
    overcost = 0
    
    i = 0
    while i < len(c):
        
        for j in range(k):
            if i >= len(c): return ans
            ans += c[i] * (overcost + 1)
            i += 1
        
        overcost += 1
    
    return ans
        
        
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
