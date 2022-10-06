

from json import load
with open("countrydata.json",encoding="UTF-8") as f:
    data=load(f)
    # for c in data:
    #     print(c.get("name"))


# country_names=[c.get("name") for c in data]
# print(country_names)


# country_capital=[c.get("capital") for c in data if c.get("name")=="Ukraine"]
# print(country_capital)


         # Function for Country Details :

def get_country_details(name):
    return [c for c in data if c.get("name") == name][0]

# details=get_country_details("India")
# print(details)


          # Function for Country Capital :

# def get_country_capital(name):
#     # return [c.get("capital") for c in data if c.get("name")=="Ukraine"][0]
#     c_data=get_country_details(name)
#     if c_data:
#         return c_data.get("capital")
#
# details=get_country_capital("Pakistan")
# print(details)



          # Function for Country Population :

# def get_country_Population(name):
#     return [c.get("population") for c in data if c.get("name")=="Ukraine"][0]
#     # c_data=get_country_details(name)
#     # if c_data:
#     #     return c_data.get("population")
#
# details=get_country_Population("Ukraine")
# print(details)



          # Function for Country Currency :

# def get_country_currency(name):
    # # a=[c.get("currencies") for c in data if c.get("name")==name][0][0]
    # # return a.get('name')
    #
    # return [c.get("currencies")[0].get('name') for c in data if c.get("name")==name][0]
    #
    # # c_data=get_country_details(name)
    # # if c_data:
    # #     a=c_data.get("currencies")[0]
    # #     return a.get("name")

# details=get_country_currency("Afghanistan")
# print(details)



           # Boarder sharing countries   ( home work )

# def get_country_border_shared(name):
#     a=[c.get("borders") for c in data if c.get("name")==name][0]
#     lst=[]
#     for i in a:
#         [lst.append(c.get("name")) for c in data if c.get("alpha3Code")==i]
#     print(lst)
#
# get_country_border_shared("Afghanistan")



# def get_country_border_shared(name):
#     c_data=get_country_details(name)
#     border_list=c_data.get('borders')
#     b_names=[c.get('name') for c in data if c.get('alpha3Code') in border_list]
#     return b_names
#
# details=get_country_border_shared("Afghanistan")
# print(details)


          # Function for max: Population country:

# max_population_country=max(data,key=lambda c:c.get("population"))
# print(max_population_country)

# def get_max_populated_country():
#     c_data=max(data,key=lambda c:c.get("population"))
#     return c_data.get("name")
#
# details=get_max_populated_country()
# print(details)


          # Function for minimum Population country:

# min_population_country=min(data,key=lambda c:c.get("population"))
# print(min_population_country)

# def get_min_populated_country():
#     c_data=min(data,key=lambda c:c.get("population"))
#     return c_data.get("name")
#
# details=get_min_populated_country()
# print(details)




          # Function to get Country Language :

def get_country_language(name):
    c_data=get_country_details(name)
    # language_list=[c.get("languages")for c in data if c.get("name")==name][0]
    # language_name=[l.get("name") for l in language_list]
    # return language_name
    return [l.get('name') for l in c_data.get("languages")]
details=get_country_language("India")
print(details)


