#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    count = Counter(s)
    minimum = min(count.values())
    maximum = max(count.values())
    
    if maximum - minimum > 1 and minimum != 1:
        return "NO"
    
    countOccurs = Counter(count.values())
    print(countOccurs)
    if len(countOccurs) == 2:
        (f1, c1), (f2, c2) = countOccurs.items()
        
        if f1 < f2: 
            f1, f2 = f2, f1 #swap(f1,f2)
            c1, c2 = c2, c1 #swap(c1,c2)
        
        if (f1-f2 == 1 and (c2 == 1 or c1==1)) or (f2 == 1 and c2 == 1):
            return "YES"
        else:
            return "NO"
        
        
    elif len(countOccurs) < 2:
        return "YES"
    
    return "NO"

        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
