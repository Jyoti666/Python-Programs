import math
s=input()
s.strip()
s=s.replace(" ","")
l=len(s)
srt=math.sqrt(l)
#print(srt)
if int(srt % int(srt)==0):
    row=int(srt)
    col=int(srt)
else:
    row=int(srt)
    col=int(srt)+1
if row*col <l:
    row=col
#print(row,' ',col)
lis=[]
temp=[]
count=1
#print(s)
for i in s:
    #print(i)
    if count<=col:
        #print('count=', count,',s='+i)
        temp.append(i)
        count+=1
    else:
        #print('count=', count, ',s=' + i)
        lis.append(temp)
        del temp
        temp = []
        temp.append(i)
        count=2
        #print(lis)
#print(lis,',',count)
if count-1 <= col:
    lis.append(temp)
    #print('lis',count)

#print(lis)
#print(row,',',col)
enc=""
#print('r=',row-1,'c=',col)
for i in range(0,col):
    str=""
    j=0
    for j in range(0,row-1):
        #print(j,',',i,','+lis[j][i])
        str+=lis[j][i]
    #print(j)
    #print('s',j)
    if row>=2:
        if len(lis[j+1])>=i+1:
            str+=lis[j+1][i]
        #print(str)
    else:
        str+=lis[j][i]
    enc+=str+" "

print(enc)
