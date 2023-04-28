#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#


def countSwaps(a):
    n  = len(a)
    count = 0
    for i in range(n):
        for j in range(i,n):
            if(a[i] > a[j]):
                #print("here is i",a[i])
                #print("here is j",a[j])
                a[i],a[j] = a[j],a[i] 
                count +=1
    #print("here is the swaped",a)
    print ("Array is sorted in "+str(count)+" swaps.")
    print("First Element: "+str(a[0]))
    print("Last Element: "+str(a[n-1]))
if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
