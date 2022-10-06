

from mobile_app.models import mobiles as mob


print(len(mob))


print([m.get('name') for m in mob if m.get("band")=='5g'])


print(max(mob,key=lambda m:m.get("price")))


print(min(mob,key=lambda m:m.get("price")))


print([m.get('name') for m in mob if m.get("display")=='AMOLED'])


mob.sort(key=lambda m:m.get("price"))
print(mob)


mob.sort(key=lambda m:m.get("price"),reverse=True)
print(mob)


print([m.get('name') for m in mob if m.get('band')=='5g' and m.get('brand')=='samsung'])


sam=[m for m in mob if m.get("brand")=="samsung"]
costly_sam=max(sam,key=lambda m:m.get("price"))
print(costly_sam.get("name"))


