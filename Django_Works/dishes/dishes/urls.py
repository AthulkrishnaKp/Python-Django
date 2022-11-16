"""dishes URL Configuration

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
from dish.views import AddDishView,DishListView,DishDetailView,DishDeleteView,LoginFormView,RegistrationFormView,DishUpdateView,signout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',LoginFormView.as_view(),name='signin'),
    path('register/',RegistrationFormView.as_view(),name="register"),
    path('add_dishes/',AddDishView.as_view(),name="dish-add"),
    path('dishlist/',DishListView.as_view(),name="dish-all"),
    path("dishlist/<int:id>",DishDetailView.as_view(),name="dish-detail"),
    path("dishlist/<int:id>/delete",DishDeleteView.as_view(),name="dish-delete"),
    path("dishlist/change/<int:id>",DishUpdateView.as_view(),name="dish-update"),
    path("logout",signout_view,name='signout'),
]
