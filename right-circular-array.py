#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the circularArrayRotation function below.
def circularArrayRotation(a, k):
    for i in range(k):
        temp = a[0]
        for j in range(len(a) - 1):
            # temp2=a[j+1]
            # a[j+1]=temp
            # temp=temp2
            temp, a[j + 1] = a[j + 1], temp
        a[0] = temp

    return a


nkq = input().split()

n = int(nkq[0])

k = int(nkq[1])

q = int(nkq[2])

a = list(map(int, input().rstrip().split()))

# queries = []
# result = circularArrayRotation(a, k)
for i in range(0, q):
    ip = int(input())
    res=ip-k
    if res >=0:
        print(a[res])
    else:
        print(a[abs(n+res)])
    # print(result[int(input())])
    # queries_item = int(input())
    # queries.append(queries_item)

# result = circularArrayRotation(a, k, queries)

# for i in result:
# print(result)

