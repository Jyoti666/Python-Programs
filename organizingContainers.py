q=int(input())
nList=[]
matrixList=[]
for i in range(0,q):
    nList.append(int(input()))
    sList=[]
    for j in range(0,nList[i]*nList[i]):
        sList.append(int(input()))
    matrixList.append(sList)

for i in range(0,len(nList)):

print(matrixList)