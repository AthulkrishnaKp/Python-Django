

                             # HOMEWORK

# total no of movies

# print all unique genres

# movie names released in 2015

# in which year most number of movies released

from json import load
with open("movies.json",encoding="UTF-8") as f:
    data=load(f)
    # for c in data:
    #      print(c.get("title"))


# def get_movie_details(name):
#     return [c for c in data if c.get("title") == name][0]
#
# details=get_movie_details("Bad Asses on the Bayou")
# print(details)


def get_no_movies():
    return len(data)

details=get_no_movies()
print(details)





def get_unique_movie_genres():
     g_list=[c.get("genres" ) for c in data]
     lst=[]
     for i in g_list:
         if i in lst:
             pass
         elif len(i)>1:
             for g in i:
                 lst1=[g]
                 if lst1 in lst:
                     pass
                 else:
                     lst.append(lst1)
         else:
            lst.append(i)
     return lst

details=get_unique_movie_genres()
print(details)



def get_movies_in_2015():
    return [c.get("title") for c in data if c.get("year")==2015]

details=get_movies_in_2015()
print(details)



def get_year():
    years=[c.get("year") for c in data]
    y={}
    for i in years:
        if i in y:
            y[i]+=1
        else:
            y[i]=1
    # print(y)
    # for i in y:
    #     if y[i]==max(y.values()):
    #          print([i])
    return [i for i in y if y[i]==max(y.values())]

details=get_year()
print(details)