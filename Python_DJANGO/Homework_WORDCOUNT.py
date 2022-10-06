# pattern="ABAABCBBBB"
# FIRST RECURSIVE CHARACTER
# MOST RECURSIVE CHARACTER

def firstrec(str):
    dict={}
    for i in str:
        if i in dict:
            print("First Recursive Character is :",i)
            break
        else:
            dict[i]=1

firstrec("ABAABCBBBB")

def mostrec(str):
    dict={}
    for i in str:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    if max(dict.values()):
        print("Most Recursive Character is :",i)

mostrec("ABAABCBBBB")


