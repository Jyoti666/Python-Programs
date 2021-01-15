s,n=list(map(int,input().rstrip().split()))
arr=list(map(int,input().rstrip().split()))

res=[]
#for i in range(0,len(arr)-1):
    #print(i)
i=0
res.append(arr[i])
for j in range(i+1,len(arr)):
        #print(j)
    if((arr[i]+arr[j])%n != 0):
        if(len(res) ==0):

            res.append(arr[j])
        else:
            valid=True
            #print(res)
            for k in res:
                if((arr[j]+k)%n ==0):
                    valid=False
                    break
            #print(arr[j],' ,',valid)
            if(valid):

                res.append(arr[j])
    print(res)
#print(len(list(set(res))))
print(res)
print(len(list(set(res))))




"""
def nonDivisibleSubset(k, arr):
    resid_cnt = [0] * k

    for el in arr:
        resid_cnt[el % k] += 1
        print(el,'%',k,'=',el%k,'+',1)
    print(resid_cnt)
    res = min(1, resid_cnt[0])
    for ind in range(1, (k // 2) + 1):
        if ind != k - ind:
            res += max(resid_cnt[ind], resid_cnt[k - ind])

    if k % 2 == 0 and resid_cnt[int(k / 2)] != 0:
        res += 1

    return res


if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    arr = list(map(int, input().strip().split(' ')))
    result = nonDivisibleSubset(k, arr)
    print(result)"""