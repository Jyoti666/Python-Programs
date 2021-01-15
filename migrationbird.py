n=int(input())
list1=input().split()
list2=[]
for i in list1:
    if i not in list2:
        list2.append(i)
list3=[]
for i in range(0,int(max(list1))):
    if str(i+1) in list2:
        list3.append(list1.count(str(i+1)))
    else:
        list3.append(0)
print(list3.index(max(list3))+1)