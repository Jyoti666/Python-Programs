n=int(input())
if(n>1 and n < 1000001):
    s=input()
    if (s.count('U')+s.count('D')) == n:
        climb=valley=0
        for i in s:
            if i == 'U':
                climb+=1
                if climb==0 and i=='U':
                    valley+=1
            else:
                climb-=1
        print(valley)