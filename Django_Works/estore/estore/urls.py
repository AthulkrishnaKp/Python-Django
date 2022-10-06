"""estore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# from api.views import ProductsView,MorningView,EveningView,
# AddView,Sunstraction,Multiplication
# from api.views import Cubeview,Numcheck,Factorialview,
# Wordcountview,Pallindromview,Primenumberview,Armstrongview,ProductsView
# from api.views import ProductsView,ProductDetailsView,Reviewsview,
#     ReviewDetailsView,ProductsViewsetView
from api.views import ProductModelViewsetView,ReviewModelViewsetView,UserView
from rest_framework.authtoken.views import ObtainAuthToken

from rest_framework.routers import DefaultRouter
router=DefaultRouter()
# router.register("api/v1/products",ProductsViewsetView,basename="products")
router.register("api/v2/products",ProductModelViewsetView,basename="books")
router.register("api/v2/reviews",ReviewModelViewsetView,basename="reviews")
router.register("register",UserView,basename="user")
# localhost:8000/products

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/', ObtainAuthToken.as_view())

    # path('cube',Cubeview.as_view()),
    # path("numchk",Numcheck.as_view()),
    # path("factorial",Factorialview.as_view()),
    # path("wordcount",Wordcountview.as_view()),
    # path("pallindrom",Pallindromview.as_view()),
    # path("prime",Primenumberview.as_view()),
    # path("armstrong",Armstrongview.as_view()),

    # path("products",ProductsView.as_view()),
    # path("products/<int:id>",ProductDetailsView.as_view()),
    # path("reviews",Reviewsview.as_view()),
    # path("reviews/<int:id>",ReviewDetailsView.as_view())

    # path('products',ProductsView.as_view()),
    # path('morning',MorningView.as_view()),
    # path('evening',EveningView.as_view()),
    # path('add',AddView.as_view()),
    # path("sub",Sunstraction.as_view()),
    # path("mult",Multiplication.as_view())

]+router.urls