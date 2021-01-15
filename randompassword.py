import random
import string
def randpassword():
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(8))
print("Random Password:")
print ("First Random Password ", randpassword() )
print ("second Random Password ", randpassword() )