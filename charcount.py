print('Enter the file name : ')
filename=input()
print('Enter the character to be counted : ')
char=input().lower()
file=open(filename,'r')
str=file.read()
print()
print('Information in '+filename)
print('------------------------')
print(str)
print()
print("File '"+filename+"' has ",(str.lower()).count(char)," instances of \
letter '"+char+"'.")