file=open('inputFile.txt','r')
mylist=file.read()
print(mylist)
print()
mylist=mylist.split("\n")
str=""
for i in mylist:
    str+=" "+i
mylist=list(str.split())
mylist2=list(dict.fromkeys(mylist))
mylist2.sort()
for i in mylist2:
    print(i+' : ',mylist.count(i))
