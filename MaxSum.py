N,W,D=map(int,input().split())
arr=list(map(int,input().rstrip().split()))
sum1=0
sum2=0
arr2=arr
#print(W)
for i in range(0,int(len(arr)/(W+1))):

    for j in range(0,int(len(arr)/W)):
        small=min(arr[i:W+1])
        arr[arr[i:W+1].index(small)]=0
print(int(len(arr2)/(abs(W+D)+1)))
for i in range(0,int(len(arr2)/(abs((W+D))+1))):
    for j in range(0,int(len(arr)/abs((W+D))+1)):
        small=min(arr[i:W+1])
        arr[arr2[i:W+1].index(small)]=0

print(arr2)