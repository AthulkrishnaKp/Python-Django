text="hello hai hello hai hai you"

words=text.split(" ")
print(words)
wc={}
for w in words:
    if w in wc:
        wc[w]+=1
    else:
        wc[w]=1

print(wc)



pattern="ABCABBDD"

wc={}
for char in pattern:
    if char in wc:
        print("First recursive character is :",char)
        break
    else:
        wc[char]=1


