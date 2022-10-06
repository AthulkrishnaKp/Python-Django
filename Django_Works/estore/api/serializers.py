
from rest_framework import serializers
from api.models import Books,Carts
from api.models import Reviews
from django.contrib.auth.models import User


class ReviewSerializer(serializers.ModelSerializer):
    create_date=serializers.CharField(read_only=True)
    class Meta:
        model=Reviews
        # fields=["book","user","comment","rating"]
        # exclude=("created_date",)  #  ( , given after create_date to make it a tuple)
        fields="__all__"

class BookModelSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)  # ( to show id in output 'read only' )
    class Meta:
        model=Books
        fields="__all__"
        # fields=["name","publisher",....]  or

class CartSerializer(serializers.ModelSerializer):
    book=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)
    status=serializers.CharField(read_only=True)
    class Meta:
        model=Carts
        field=["book","user","status"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["first_name","last_name","username","email","password"]

    def create(self,validated_data):
        return User.objects.create_user(**validated_data)        # (This step is to encrypt password and then save)











###################################################################################



# class BookSerializer(serializers.Serializer):
#     id=serializers.CharField(read_only=True)
#     name=serializers.CharField()
#     author=serializers.CharField()
#     price=serializers.IntegerField()
#     publisher=serializers.CharField()
#     qty=serializers.IntegerField()
#
#     def create(self, validated_data):
#         return Books.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name=validated_data.get("name")
#         instance.author=validated_data.get("author")
#         instance.price=validated_data.get("price")
#         instance.publisher=validated_data.get("publisher")
#         instance.qty=validated_data.get("qty")
#         instance.save()
#         return instance
        # return Books.objects.update(**validated_data)





# TWO TYPES OF VALIDATIONS
#1 FIELD LEVEL VALIDATION

    # def validate_price(self,value):
    #     if value not in range(50,1000):
    #         raise serializers.ValidationError("invalid price")
    #     return value
    # def validate_qty(self,value):
    #     if value not in range(1,500):
    #         raise serializers.ValidationError("invalid quantity")
    #     return value



#2 OBJECT LEVEL VALIDATION

    # def validate(self,data):             # (giving ranges for certains things we use validate )
    #     err_list=[]
    #     qty=data.get("qty")
    #     price = data.get("price")
    #     if qty not in range(1,500):
    #         raise serializers.ValidationError()
    #         # err_list.append("invalid quantity")
    #     if price not in range(50,1000):
    #         # raise serializers.ValidationError("invalid price")
    #         err_list.append("invalid price")
    #     if err_list:
    #         raise serializers.ValidationError(err_list)
    #     return data
