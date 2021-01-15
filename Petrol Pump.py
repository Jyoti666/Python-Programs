p=input().split()
petrol=[]
for i in p:
    petrol.append(int(i))
petrol.sort()
del p
petrol1=[]
petrol2=[]
for i in range(0,int(len(petrol)/2)):
    petrol1.append(petrol[i])
for i in range(int(len(petrol)/2),len(petrol)):
    petrol2.append(petrol[i])
petrol2.sort(reverse=True)

a=0
b=0
print(petrol1)
print(petrol2)
for i in range(0,int(len(petrol1)/2)):
    print(a,"=",petrol1[i],"+",petrol2[i])
    a+=petrol1[i]+petrol2[i]
    print(a)
for i in range(int(len(petrol1)/2),len(petrol1)):
    print(b, "=", petrol1[i], "+", petrol2[i])
    b+=petrol1[i]+petrol2[i]
    print(b)
if a>b:
    print(a)
else:
    print(b)


