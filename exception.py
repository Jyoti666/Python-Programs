try:
    a=10
    b=2
    c=a/b
except ZeroDivisionError,IOError:
    print("Invalid Denominator")
else:
    print('Else')
finally:
    print("I will do my job")