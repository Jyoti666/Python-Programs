file=open('string.txt','w')
file.write(input('Enter a string:'))
file.close()

file=open('string.txt','r')
list=[]
list.append(file.read().split(' '))
longest= list[0][0]
for i in list[0]:
    if len(i) > len(longest):
        longest=i
print('LONGEST WORD :'+longest)
file.close()