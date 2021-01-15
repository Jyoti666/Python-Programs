dlist=[["amy",100],["david",100],["heraldo",50],["aakansha",75],["aleska",150]]
nameList=[]
scoreList=[]

for i in dlist:
    temp=i[0]
    i[0]=i[1]
    i[1]=temp

dlist.sort(reverse=True)


for i in dlist:
    scoreList.append(i[0])

for i in dlist:
    nameList.append(i[1])
listscores=[]
#print(nameList)
listscores=list(set(scoreList))
listscores.sort(reverse=True)

count=0
sortList=[]
for i in listscores:
    for j in range(count,scoreList.count(i)):
        sortList.append(nameList[j])
    sortList.sort()
    temp = 0
    #print("sortList",sortList)
    for k in range(count,scoreList.count(i)):
        dlist[k][1]=sortList[temp]
        temp+=1
        count = scoreList.count(i)
        sortList=[]
#print(dlist)

for i in dlist:
    print(i[1]+" ",i[0])

