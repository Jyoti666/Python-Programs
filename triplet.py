"""list=input().split(" ")
n,r=int(list[0]),int(list[1])
ind,count=0,0
del list
list=[]
list2=input().split(" ")

for i in range(0,n):
    list.append(int(list2[i]))

for i in range(0,n-2):
    print("For",list[i])
    ind=0
    proceed=0
    ind2=list.index(list[i]*r)
    occurence=0
    while proceed==0:
        #print("list[ind:n]",list[ind:n])
        print("list[i]", list[i])
        if list[i]*r in list[ind2:n]:
            print("list[i]*r=",list[i]*r)
            print("list[ind:n]=",list[ind:n])
            if (list[i]*r)*r in list[ind:n]:
                print("list[i]*r*r",list[i]*r*r," Count= ",list.count(list[i]*r*r))
                count+=1
                #print(list)
                ind=list.index(list[i]*r*r,ind,n)+1
                print("ind=",ind)
                occurence+=1
                print("count=",count)
                if occurence==list.count(list[i]*r*r) and list[i]*r in list[ind2+1:n] :
                    ind2=list.index(list[i]*r,ind2+1,n)
                    ind=0
                    occurence=0
                    print("ind=",ind)
                    print("list[ind2+1:n]=",list[ind2:n])
                    print("list[i]*r=",list[i]*r)
                    print("ind2=",ind2)
                    print("inner if")
                    if ind2==0:
                        print("inner ind2")
                        proceed=1


            else:
                print("else 1")
                proceed=1
        else:
            #print(i, ",", r)
            print("else-2")
            proceed=1
print("kk")
print(count)
print("ll")"""

list=input().split(" ")
n,r=int(list[0]),int(list[1])
ind,count=0,0
del list
list=[]
list2=input().split(" ")
for i in range(0,n):
    list.append(int(list2[i]))
for i in range(0,n-2):
    ind=0
    proceed=0
    ind2=list.index(list[i]*r)
    occurence=0
    while proceed==0:
        if list[i]*r in list[ind2:n]:
            if (list[i]*r)*r in list[ind:n]:
                count+=1
                ind=list.index(list[i]*r*r,ind,n)+1
                occurence+=1
                if occurence==list.count(list[i]*r*r) and list[i]*r in list[ind2+1:n] :
                    ind2=list.index(list[i]*r,ind2+1,n)
                    ind=0
                    occurence=0
                    if ind2==0:
                        proceed=1
            else:
                proceed=1
        else:
            proceed=1
print(count)
