#file
#fileobject=open(file_name,mode)
#Mode

# r  - Read
# r+ - Read,Write
# w  - write
# w+ - read,write
# a  - append

# read-read from file

# f1=open("File1","r")
# print("First location:",f1.tell())
# print(f1.read(3))
# print("Second location:",f1.tell())
# print(f1.read(3))
# print("Third locationf1.close():",f1.seek(0))  # To go to required location
# print(f1.read(3))
# f1.close()


# f1=open("File1","r")
# print(f1.read(3))
# f1.close()

# READ LINE
# f1=open("File1","r")
# print(f1.readline())    # reads a complete line
# f1.close()

# f1=open("File1","r")
# # print(f1.readlines())    # reads all lines and displays as a list.
# for i in f1.readlines():
#     print(i.strip())
# f1.close()



# f1=open("File1","w+")
# f1.write("Hello how")    # file 1 gets overwritted and only exists "Hello how are you" now.
# print(f1.read(9))
# f1.close()


# f1=open("File1","w")
# lst=['Hello\n','how are you\n','where are you\n']
# f1.writelines(lst)
# f1.close()

# f1=open("File1","r")
# a=f1.read()
# print(a)
# f2=open("File2","w")
# f2.write(a)
# f1.close()
# f2.close()


# Number of words in File .

# f1=open("File1",'r')
# read=f1.read()
# print(read)
# print(read.split())
# words=read.split()
# # c=0
# # for i in words:
# #     c=c+1
# # print(c)
# print(len(words))

#only unique words .

# f1=open("File1",'r')
# read=f1.read()
# print(read)
# print(read.split())
# words=set(read.split())
# print(words)
# # c=0
# # for i in words:
# #     c=c+1
# # print(c)
# print(len(words))

# how many words and count of each word in file.




# ********************* IMPORTANT INTERVIEW **********************


def wordcount(word):   # [word] any variable should be passed in a function.
    dict={}
    for i in words:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    print(dict)
    for k,v in dict.items():
        print(k,":",v)


f1=open("File1",'r')
r=f1.read()
words=r.split()
print(words)
wordcount(words)
