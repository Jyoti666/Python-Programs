#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    l_r=r_r=t_c=b_c=t_l_c=t_r_c=b_l_c=b_r_c=0
    #print(9)
    #l_r
    if c_q - 1 != 0:
        for i in range(c_q - 1, 0,-1):
            """if i == 0:
                break"""
            if [r_q,i] in obstacles:
                break
            else:
                l_r += 1

        print("l_r :",l_r)

    if c_q !=n:
        for i in range(c_q +1, n+1):

            if [r_q, i] in obstacles:
                break
            else:
                r_r += 1

        print("r_r :",r_r)
    if r_q != n:

        for i in range(r_q +1,n+1):

            if [i,c_q] in obstacles:
                break
            else:
                t_c += 1

        print("t_c :",t_c)
    if r_q != 1:

        for i in range(r_q -1,0,-1):

            if [i,c_q] in obstacles:
                break
            else:
                b_c += 1

        print("b_c :",b_c)

    temp=c_q - 1
    if r_q != n:

        for i in range(r_q +1,(c_q-1)+r_q+1):
            if i > n:
                break
            if [i,temp] in obstacles:
                break
            else:
                t_l_c += 1
                temp -= 1

        print("t_l_c :",t_l_c)

    temp = c_q + 1
    if r_q != n:

        for i in range(r_q + 1, n + 1):

            if [i, temp] in obstacles:
                break
            else:
                t_r_c += 1
                temp += 1

        print("t_r_c :",t_r_c)

    temp = c_q - 1
    if r_q != 1:

        for i in range(r_q - 1, (r_q-(c_q -1))-1,-1):

            if [i, temp] in obstacles:
                break
            else:
                b_l_c += 1
                temp -= 1

        print("b_l_c :",b_l_c)

    temp = r_q - 1
    if temp != 0:

        for i in range(c_q + 1, n+1):

            if [temp,i] in obstacles:
                break
            else:
                b_r_c += 1
                temp -= 1

        print("b_r_c :",b_r_c)

    return l_r+r_r+t_c+b_c+t_l_c+t_r_c+b_l_c+b_r_c
nk = input().split()

n = int(nk[0])

k = int(nk[1])

r_qC_q = input().split()

r_q = int(r_qC_q[0])

c_q = int(r_qC_q[1])

obstacles = []

for _ in range(k):
    obstacles.append(list(map(int, input().rstrip().split())))
#print(obstacles)
result = queensAttack(n, k, r_q, c_q, obstacles)

print(result)