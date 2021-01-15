#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the utopianTree function below.
def utopianTree(n):
    print("n :",n)
    growth = 0
    bug = []
    if n == 0:
        return 1
    else:
        valid = True
        while (valid == True):
            #print(valid)
            growth += 1
            bug.append(growth)
            growth += growth
            bug.append(growth)
            n -= 2
            #print("n=",n)
            #print("n % 2 == 1 or n % 2 == 0",n % 2 == 1 or n % 2 == 0)
            #print("valid = ",(n % 2 == 1 or n % 2 == 0) and n !=0 and n>=0)
            valid=((n % 2 == 1 or n % 2 == 0) and n !=0 and n>=0)
        if n == 0:
            print("lllll")
            bug.append(growth + 1)
            return bug
        else:
            return bug



t = int(input())
if t > 0 and t < 11:
    for t_itr in range(t):
        n = int(input())
        if n >= 0 and n < 61:
            result = utopianTree(n)

            print(str(result) + '\n')
        else:
            sys.exit()

