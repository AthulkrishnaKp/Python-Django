
# ...................... NOT VERY IMPORTANT ....................

import re

f1=open('File1','r')
text=f1.readlines()
for i in text:                             # '.' matches any single character
    result=re.search(r'\bs.e\b',i)         # starting letter must be 's' and ending letter is 'e'
    if result:                             # \b represents space starting and after so shed will not be read.
        print(i)

# ...................... NOT VERY IMPORTANT ....................

import re

f1=open('File1','r')
text=f1.readlines()
for i in text:                             # \w* matches any number of characters between s and e .
    result=re.search(r'\bs\w*e\b',i)       # starting letter must be 's' and ending letter is 'e' in between many letters can be read.
    if result:                             # \b represents space starting and after so shed will not be read.
        print(i)                           # \w represent number of words .
                                           # eg: shoe,showne,soone all can be read