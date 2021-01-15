N=int(input())
if(N>=1 and N<=100):
    arr=list(map(int,input().rstrip().split(" ")))

    dict={0:2,1:2,2:1,3:2,4:2,5:2,6:1,7:2,8:2,9:2}
    dict2={'0':'zero','1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine'}
    vowel=0
    for i in arr:
        vowel+=dict[i]

    pair=0
    for i in range(0,N):
        temp=i
        for j in range(i+1,N):
            temp+=j
            if(temp == vowel):
                pair+=1
                break
            elif(temp > vowel):
                break
    txt=''
    pair=str(pair)
    for i in pair:
        txt+=dict2[i]
    print(txt)