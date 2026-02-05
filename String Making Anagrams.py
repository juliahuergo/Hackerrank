#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'makeAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def makeAnagram(a, b):
    countA = Counter(a) 
    countB = Counter(b) 
    
    letters = set(a)
    letters.update(b)
    
    deletions = 0
    
    for letter in letters:
        deletions += abs(countA[letter] - countB[letter])
    
    return deletions
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
