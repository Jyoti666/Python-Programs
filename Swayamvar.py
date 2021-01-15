N=int(input())
if(N >=1 and N<=1000):
    brides_drunk=input()
    if(len(brides_drunk) == N):
        brides_to_be=[]
        for i in brides_drunk:
            brides_to_be.append(i)

        grooms_drunk = input()
        if(len(grooms_drunk) == N):
            grooms_to_be = []
            for i in grooms_drunk:
                grooms_to_be.append(i)

            res=0
            temp=N
            repeat=True
            for i in brides_to_be:
                if repeat:
                    repeat=False
                    count=0

                    j=0
                    while j < N:
                        if count == temp:
                            break
                        else:
                            count += 1
                            if i == grooms_to_be[j]:
                                res+=1
                                del grooms_to_be[j]
                                N-=1
                                temp-=1
                                repeat=True
                                break
                            else:
                                grooms_to_be.append(grooms_to_be[j])
                                del grooms_to_be[j]
            print(N)