num=input()
if(len(num) >=1 and len(num) <= 1000):
    res=" "
    #res=[]
    for i in range(0,10):
        if str(i) in num:
            res+=' '+str(num.count(str(i)))
            #res.append(num.count(str(i)))

        else:
            #res.concat(str(i))
            res+=" 0"
            #res.append(0)
    print(res)
    """for i in res:
        print(i,end=" ")"""