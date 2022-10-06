

from frameworks.models import frameworks as fws

# print([fw for fw in fws])

#print all frameworks names ?

# print([fw.get("name") for fw in fws])

#print all frameworks name whose language is python ?

# print([fw.get('name') for fw in fws if fw.get('language')=="python"])

#print fws names whose rating>4 ?

# print([fw.get('name') for fw in fws if fw.get('rating')>4])

#print names of all backend technologies ?

# print([fw.get('name') for fw in fws if fw.get('belongsto')=='backend'])

#print details of top rated framework ?

# top_rated_fw=max(fws,key=lambda fw:fw.get("rating"))
# print(top_rated_fw)

#print details of lowest rated framework ?

# lowest_rated_fw=min(fws,key=lambda fw:fw.get("rating"))
# print(lowest_rated_fw)

#sort framewprks by rating descending order ?

fws.sort(key=lambda fw:fw.get('rating'),reverse=True)
print(fws)     # reverse=True to get descending order






