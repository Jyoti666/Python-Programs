str=input('Enter String:')
list=list(str)
for i in range(0,len(list)):
    if list[i].islower():
        list[i]=list[i].upper()
    else:
        list[i]=list[i].lower()
print(''.join(list))