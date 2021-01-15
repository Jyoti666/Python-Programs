file=open('mix.txt','r')
text=file.read()
print(text)
print()
number=[]
vowel=[]
for i in text:
    if i.isdigit() == True:
        number.append(i)
    elif i in 'a,e,i,o,u':
        vowel.append(i)
print('NUMBERS : ',number)
print('VOWELS : ',vowel)

