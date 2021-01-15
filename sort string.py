"""list=[["a",5],["d",1],["a",2],["a",1],["b",3]]
def func(e):
    return e[1]
list.sort(reverse=True,key=func)
print(list)
list.reverse()
print(list)"""
a=int(input())
list=[]
for i in range(0,5):
    temp=input().split(" ")
    temp[1]=int(temp[1])
    list.append(temp)
def func(e):
    return e[1]
list.sort(key=func)
for i in list:
    print(i[0]+" ",i[1])