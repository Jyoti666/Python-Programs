import sys
#print(len(sys.argv))
sum=0
for i in range(len(sys.argv)-1):
    sum=sum+int(sys.argv[i+1])

print('avg: ',sum/(len(sys.argv)-1))