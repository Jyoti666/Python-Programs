file=open('file','r')

file2=open('file2.txt','w')
file2.write(file.read())
file2.close()

file2=open('file2.txt','r')
print(file2.read())
print()
file2.close()

file2=open('file2.txt','r')
text=file2.read()
print('LINES :',len(text.split('\n')))
print('WORDS :',len(text.split(' '))+int((len(text.split('.'))-1)/2))
vowel=0
consonant=0
for i in text:
    if i.lower() in 'a,e,i,o,u':
        vowel += 1
    elif i.lower() in 'b,c,d,f,g,h,j,k,l,m,n,p,q,r,s,t,v,w,x,y,z':
        consonant += 1
print('VOWELS :',vowel)
print('CONSONANT :',consonant)
file2.close()
