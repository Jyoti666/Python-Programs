#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    j=0
    e=100
    j+=k
    while(j<len(c)):
        if c[j] ==0:
            e-=1
            print('1')
        else:
            e-=3
            print('2')
        j+=k
    if (j-(len(c)-1)) < k:
        return e-1
    else:
        return e
n=1
if n==1:

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    print(result)
