#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
        val = arr[n-1]
        for j in range(n-2,-1,-1):
            stri = ""
            if (val < arr[j] and j!=0):
                arr[j+1] = arr[j]
                for i in range(n):
                    if(i==n-1):
                        stri += str(arr[i])
                    else:
                        stri += str(arr[i])+" "
                print(stri)
            elif(j==0 and val < arr[j]):
                arr[1] = arr[0]
                for i in range(n):
                    if(i == n-1):
                        stri +=str(arr[i])
                    else:
                        stri +=str(arr[i])+" "
                print(stri)
                stri = ""
                arr[0] = val
                for i in range(n):
                    if(i == n-1):
                        stri +=str(arr[i])
                    else:
                        stri +=str(arr[i])+" "
                print(stri)
                break
            else:
                arr[j+1] = val
                for i in range(n):
                    if(i == n-1):
                        stri +=str(arr[i])
                    else:
                        stri +=str(arr[i])+" "
                print(stri)
                break
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
