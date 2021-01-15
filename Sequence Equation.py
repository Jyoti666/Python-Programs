#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the permutationEquation function below.
def permutationEquation(p):
    a=[]
    for x in range(1,len(p)+1):
        a.append(p.index(p.index(x)+1)+1)
    return a
n = int(input())

p = list(map(int, input().rstrip().split()))

result = permutationEquation(p)

print(result)
