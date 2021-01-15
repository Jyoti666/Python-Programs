
import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    res =[]
    while(len(a )!=1 and len(a )!=0):
        temp1 =[]
        temp2 =[]
        temp1.append(a[0])
        temp2.append(a[0])
        b=a
        for i in a[1:len(a)]:
            if(i == a[ 0]):
                temp1.append(i)
                temp2.append(i)
                del b[(b[1:len(a)].index(i))+1]

            elif(i == a[ 0]+1):
                temp1.append(i)

                del b[b.index(i)]
            elif(i == a[ 0]-1):
                temp2.append(i)

                del b[b.index(i)]


        del b[0]
        a=b

        res.append(temp1)

        temp3=temp2
        if(len(list(set(temp3)))==2):
            res.append(temp2)


    maxsize= len(res [0])
    for i in res[1:len(res)]:
        if len(i)>maxsize :
            maxsize=len(i)

    return maxsize



n = int \


(input().strip())

a = list(map(int, input().rstrip().split()))

result = pickingNumbers(a)

print(result)
