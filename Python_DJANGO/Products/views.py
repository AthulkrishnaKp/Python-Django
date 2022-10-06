
from Products.models import items


# List,details,create,update

# list()
# create()
# retrieve()        " specificly take some items "
# update()
# destroy()         " These are predefined function names used for lists on oops "


class Products:

    def list(self, *args, **kwargs):
        all_products = items
        if "category" in kwargs:
            cat = kwargs.get("category")
            all_products = [p for p in all_products if p.get("category") == cat]
        return all_products

    def retrieve(self, *args, **kwargs):
        # print(kwargs)
        id = kwargs.get("id")
        # print(id)
        item = [i for i in items if i.get("id") == id]
        return item

    def destroy(self, *args, **kwargs):
        id = kwargs.get("id")
        item = [i for i in items if i.get("id") == id][0]  # [0] to get element from list that is here dictionary
        # print(item)
        items.remove(item)
        return item

    def create(self, *args, **kwargs):
        data = kwargs.get("data")
        items.append(data)
        return data

    def update(self, *args, **kwargs):
        print(kwargs)
        id = kwargs.get("id")
        data = kwargs.get("data")
        instance = [i for i in items if i.get("id") == id][0]  # [0] to get element from list that is here dictionary
        instance.update(data)
        return instance


p = Products()

# List()

# print(p.list())
# print(p.list(category="electronics"))


# Retrieve()

# print(p.retrieve(id=15))


# Destroy()

# print(p.destroy(id=1))
# print(p.list())


# Create()

# data={
# "id": 21,
#     "title": "Watch",
#     "price": 24000,
#     "description": "Your perfect Watch",
#     "category": "electronics",
#     "image": "https://fakestoreapi.com/img/81fPKd-2AYL._AC_SL1500_.jpg",
#     "rating": {
#       "rate": 3.9,
#       "count": 120
#     }
# }
# print(p.create(data=data))
# print(p.list())


# Update()

data = {
    "price": 3000,
    "description": "Perfect"
}
print(p.update(id=1, data=data))


