from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Books,Reviews,Carts
from api.serializers import ReviewSerializer,BookModelSerializer,UserSerializer,CartSerializer
# from api.serializers import BookSerializer
# from rest_framework.viewsets import ViewSet
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from rest_framework import authentication,permissions
from rest_framework.decorators import action



class ProductModelViewsetView(ModelViewSet):
    # authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = BookModelSerializer
    queryset = Books.objects.all()

    @action(methods=["POST"],detail=True)
    def add_review(self,request,*args,**kwargs):
        #  localhost:8000/api/v2/products/1/add_review/
        id=kwargs.get("pk")
        book=Books.objects.get(id=id)
        Reviews.objects.create(book=book,user=request.user,
                               comment=request.data.get("comment"),
                               rating=request.data.get("rating"))
        return Response(data="created")

    @action(methods=["POST"],detail=True)
    def addto_cart(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        book=Books.objects.get(id=id)
        Carts.objects.create(book=book,user=request.user)
        return Response(data="created")


    @action(methods=["GET"],detail=True)
    def cart_list(self,request,*args,**kwargs):
        cart=Carts.objects.all()
        cart_list=cart.books_set.all()
        serializer=CartSerializer(cart_list,many=True)
        return Response(data=serializer.data)


    #  localhost:8000/api/v2/products/1/get_review/
    @action(methods=["GET"],detail=True)
    def get_review(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        book=Books.objects.get(id=id)
        reviews=book.reviews_set.all()
        serializer=ReviewSerializer(reviews,many=True)
        return Response(data=serializer.data)



class ReviewModelViewsetView(ModelViewSet):
    serializer_class = ReviewSerializer
    queryset = Reviews.objects.all()
    def list(self, request, *args, **kwargs):
        all_reviews=Reviews.objects.all()
        # print(request.query_params)
        if 'user' in request.query_params:
            all_reviews=all_reviews.filter(user=request.query_params.get("user"))
        serializer = ReviewSerializer(all_reviews, many=True)
        return Response(data=serializer.data)

class UserView(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


################################################################################

#
#
# class ProductsViewsetView(ViewSet):
#
#
#     def list(self,request,*args,**kwargs):
#         qs=Books.objects.all()
#         serializer=BookSerializer(qs,many=True)
#         return Response(data=serializer.data)
#
#     def create(self,request,*args,**kwargs):
#         serializer=BookSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data)
#         else:
#             return Response(data=serializer.errors)
#
#     def retrieve(self,request,*args,**kwargs):
#         id=kwargs.get("pk")
#         book=Books.objects.get(id=id)
#         serializer=BookSerializer(book,many=False)
#         return Response(data=serializer.data)
#
#     def update(self,request,*args,**kwargs):
#         id=kwargs.get("pk")
#         book=Books.objects.filter(id=id)
#         serializer=BookSerializer(instance=book,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data)
#         else:
#             return Response(data=serializer.errors)
#
#     def destroy(self,request,*args,**kwargs):
#         id=kwargs.get("pk")
#         Books.objects.get(id=id).delete()
#         return Response(data="Deleted")
#

# class ProductsView(APIView):
#     def get(self,request,*args,**kwargs):
#         return Response({"msg":"inside products get"})
#
# class MorningView(APIView):
#     def get(self,request,*args,**kwargs):
#         return Response({"msg":"good morning"})
#
# class EveningView(APIView):
#     def get(self,request,*args,**kwargs):
#         return Response({"msg":"good evening"})
#
# class AddView(APIView):
#     def post(self,request,*args,**kwargs):
#         n1=request.data.get("num1")
#         n2=request.data.get("num2")
#         res=int(n1)+int(n2)
#         return Response({"Result":res})
#
# class Sunstraction(APIView):
#     def post(self,request,*args,**kwargs):
#         n1=request.data.get("num1")
#         n2=request.data.get("num2")
#         res=int(n1)-int(n2)
#         return Response({"Result":res})
#
# class Multiplication(APIView):
#     def post(self,request,*args,**kwargs):
#         n1=request.data.get("num1")
#         n2=request.data.get("num2")
#         res=int(n1)*int(n2)
#         return Response({"Result":res})

# class Cubeview(APIView):
#     def post(self,request,*args,**kwargs):
#         n=int(request.data.get("num"))
#         res=n**3
#         return Response({"Result":res})
#
# class Numcheck(APIView):
#     def post(self,request,*args,**kwargs):
#         n=int(request.data.get("num"))
#         res=""
#         if n%2==0:
#             # return Response({"Result":"Even number"})
#             res="Number is Even"
#         else :
#             res="Number is Odd"
#             # return Response({"Result":"Odd number"})
#         return Response({"Result":res})
#
# class Factorialview(APIView):
#     def post(self,request,*args,**kwargs):
#         n=int(request.data.get("num"))
#         fact=1
#         for i in range (1,n+1):
#             fact=fact*i
#         return Response({"Result":fact})


# class Wordcountview(APIView):
#     def post(self,request,*args,**kwargs):
#         txt=request.data.get("text")
#         lst=txt.split()
#         c=0
#         for words in lst:
#             c=c+1
#         return Response({"Number of Words":c})

# class Wordcountview(APIView):
#     def post(self,request,*args,**kwargs):
#         txt=request.data.get("text")
#         words=txt.split(" ")
#         wc={}
#         for w in words:
#             if w in wc:
#                 wc[w]+=1
#             else:
#                 wc[w]=1
#         return Response(data=wc)
#
#
# # pallindrom,prime number,armstrong number
#
#
# class Pallindromview(APIView):
#     def post(self,request,*args,**kwargs):
#         txt=request.data.get("text")
#         txt1=txt[::-1]
#         if txt1==txt:
#             res="Pallindrom"
#         else:
#             res="Not Pallindrom"
#         return Response({"Result":res})
#
#
# class Primenumberview(APIView):
#     def post(self,request,*args,**kwargs):
#         n=int(request.data.get("num"))
#         c=0
#         for i in range(1,n+1):
#             if n%i==0:
#                 c=c+1
#         if c==2:
#             res="Prime number"
#         else:
#             res="Not Prime number"
#         return Response({"Result":res})
#
#
# class Armstrongview(APIView):
#     def post(self,request,*args,**kwargs):
#         n=int(request.data.get("num"))
#         sum=0
#         num=num1=n
#         c=0
#         while n>0:
#             n=n//10
#             c=c+1
#         while num > 0:
#             d=num%10
#             sum=sum+d**c
#             num=num//10
#         if num1==sum:
#             res="Armstrong number"
#         else:
#             res="Not Armstrong number"
#         return Response({"Result": res})


# class ProductsView(APIView):
#
#     def get(self,request,*args,**kwargs):
#         qs=Books.objects.all()
#         serializer=BookSerializer(qs,many=True)
#         return Response(data=serializer.data)
#
#     def post(self,request,*args,**kwargs):
#         serializer=BookSerializer(data=request.data)       # Correct model
#         if serializer.is_valid():   # checking thet is there any errors in serializer .
#             # print(serializer.validated_data)
#             Books.objects.create(**serializer.validated_data)
#             return Response(data=serializer.data)
#         else:
#             return Response(data=serializer.errors)

        # bname=request.data.get("name")
        # bauthor=request.data.get("author")
        # bprice=request.data.get("price")
        # bpublisher=request.data.get("publisher")
        # Books.objects.create(name=bname,author=bauthor,price=bprice,publisher=bpublisher)
        # return Response(data="created")
#
# class ProductDetailsView(APIView):
#
#     def get(self,request,*args,**kwargs):
#         # print(kwargs)
#         id=kwargs.get("id")
#         book=Books.objects.get(id=id)
#         serializer=BookSerializer(book,many=False)
#         return Response(data=serializer.data)
#
#     def delete(self,request,*args,**kwargs):
#         id=kwargs.get("id")
#         Books.objects.get(id=id).delete()
#         return Response(data="Deleted")
#
#     # Update Data
#     #1 localhost:8000/products/{id}
#     #2 method put
#     #3 data={} (give data to be updated)
#
#     def put(self,request,*args,**kwargs):
#         id=kwargs.get("id")
#         serializer=BookSerializer(data=request.data)
#         if serializer.is_valid():
#             Books.objects.filter(id=id).update(**serializer.validated_data)
#             return Response(data=serializer.data)
#         else:
#             return Response(data=serializer.errors)
#
#
# # localhost:8000/reviews
# # method: get
#
# class Reviewsview(APIView):
#     def get(self,request,*args,**kwargs):
#         reviews=Reviews.objects.all()
#         serializer=ReviewSerializer(reviews,many=True)
#         return Response(data=serializer.data)
#
#     def post(self,request,*args,**kwargs):
#         serializer=ReviewSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data)
#         else:
#             return Response(data=serializer.errors)
#
#
# class ReviewDetailsView(APIView):
#     def get(self,request,*args,**kwargs):
#         id=kwargs.get("id")
#         qs=Reviews.objects.get(id=id)
#         serializer=ReviewSerializer(qs,many=False)
#         return Response(data=serializer.data)
#
#     def put(self,request,*args,**kwargs):
#         id=kwargs.get("id")
#         qs=Reviews.objects.get(id=id)
#         serializer=ReviewSerializer(instance=qs,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return  Response(data=serializer.data)
#         else:
#             return Response(data=serializer.errors)
#
#     def delete(self,request,*args,**kwargs):
#         id=kwargs.get(("id"))
#         Reviews.objects.get(id=id).delete()
#         return Response(data="Deleted")
