numbers=[10,20,10,40,50,60,70]
sum=int(input('Enter a target Number:'))
len=len(numbers)-1
proceed=1
for i in range(0,len):
    if(proceed==1):
        for j in range(i,len):
            if(numbers[i]+numbers[j]==sum and i!=j):
                proceed=0
                break
    else:
        break

if(numbers[i-1] + numbers[j] == sum):
    print('Sum of Values in indexed',i,'and',j,' are equal to target number')
else:
    print('No two values present in the array whose sum is equal to Target Number')

