import sys
p=int(input())
str=[]
text=""
for i in range(0,p*2):
    text=input()
    str.append(text)
res=[]
for i in range(0,p*2,2):
    k = str[i+1]
    op=1
    for j in range(0,len(str[i])):
        if str[i][j] in k:
            op=0
            break
    if op ==0:
        res.append("YES")
    else:
        res.append("NO")
for i in res:
    print(i)