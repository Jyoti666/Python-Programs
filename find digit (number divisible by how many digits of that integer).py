#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findDigits function below.
def findDigits(n):
    temp=n
    count=0
    while n>0:
        rem=n%10
        n=int(n/10)
        if(rem != 0):
            if (temp%rem == 0):
            #print('rem=', rem)
                count+=1
    return count

t = int(input())

for t_itr in range(t):
    n = int(input())

    result = findDigits(n)

    print(result)