import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    ans=0
    for i in range(len(s)):
        n=
        count=0
        while(n<(m)):
            print(i+n,',',s[i+n])
            count+=s[i+n]
            n+=1
        print()
        if(count==d):
            ans+=1
        if(i+n==len(s)):
            break
    return ans



n = int(input().strip())

s = list(map(int, input().rstrip().split()))

dm = input().rstrip().split()

d = int(dm[0])

m = int(dm[1])

result = birthday(s, d, m)
print(result)