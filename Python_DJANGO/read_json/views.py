
from json import load

with open("products.json",encoding="UTF-8") as f:
    data=load(f)
print(len(data))