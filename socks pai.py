import sys

n = int(input())
pair = 0
if (n >= 1 and n <= 100):
    ar = list(map(int, input().rstrip().split()))
    if len(ar) == n:
        for i in ar:
            if i < 1 or i > 100:
                sys.exit(0)
        unique = list(set(ar))
        print(unique)
        for i in unique:
            temp = int(ar.count(i) / 2)
            print(i,":",temp)
            if temp >= 1:
                pair += temp

print(pair)