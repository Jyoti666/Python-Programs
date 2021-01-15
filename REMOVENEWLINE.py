file=open('mix.txt','w')
file.write('My birth date is 16-11-1998.\n Now i am 22 years old.')
file.close()

print('Text in file:')
file=open('mix.txt','r')
text=file.read()
print(text)
file.close()

file=open('mix.txt','w')
file.write(" ".join(text.splitlines()))
file.close()

print('Text in file after removing Newline character:')
file=open('mix.txt','r')
print(file.read())
file.close()
