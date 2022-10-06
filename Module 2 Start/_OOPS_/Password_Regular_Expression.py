# Password Creating

import re
p=input("Enter a password : ")
if len(p)>=16 or len(p)<=6:
    print("Invalid password")
elif not re.search('[a-z]',p):
    print("Invalid password")
elif not re.search('[A-Z]',p):
    print("Invalid password")
elif not re.search('[0-9]',p):
    print("Invalid password")
elif not re.search("[@#&]",p):
    print("Invalid password")
else:
    print("Valid password")