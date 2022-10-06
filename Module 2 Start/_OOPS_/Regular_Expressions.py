
# Regular Expression   ( inbuild re module )
#match,search,findall,sub

# import re
# str='i like python programming'
# result=re.search('python',str)          #  SYNDAX - re.search(pattern,string)
# if result:
#     print("Pattern exists")
# else:
#     print("Pattern not exists")

# import re
# str='i like python programming'
# result=re.match('like',str)          #  SYNDAX - re.match(pattern,string)
# if result:                             # match fun only search the first word
#     print("Pattern exists")            #therefore output is pattern not exists
# else:
#     print("Pattern not exists")

# import re
# zipcode='13dr-3gf0-s3-f5'      # \d - match where str contains a digit
# new=re.findall('\d',zipcode)
# print(new)

# import re
# zipcode='1342-4434-3220-5a-35'
# new=re.sub('\d','@',zipcode)
# print(new)
#
# import re
# zipcode='1342-s45s-ssf-53-35'    # \D - match where str contains not a digit.
# new=re.sub('\D','@',zipcode)     # sub substitute when matched value to given string.
# print(new)                       # @ is substitued to all positions which is not a digit in string.

# import re
# p=input("Enter a password : ")
# if len(p)>=16 or len(p)<=6:
#     print("Invalid password")
# elif not re.search('[a-z]',p):
#     print("Invalid password")
# elif not re.search('[A-Z]',p):
#     print("Invalid password")
# elif not re.search('[0-9]',p):
#     print("Invalid password")
# elif not re.search("[@#&]",p):
#     print("Invalid password")
# else:
#     print("Valid password")
