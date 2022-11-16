from urllib import request
from django.shortcuts import render,redirect
from django.views.generic import View,UpdateView,ListView,DetailView
from django.contrib.auth.models import User
from dish.forms import LoginForm,RegistrationForm,DishUpdateForm
from dish.models import Dish
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
# Create your views here.


def signin_required(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            return redirect("signin")
        else:
            return fn(request,*args,**kwargs)    
    return wrapper


class LoginFormView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm
        return render(request,"login.html",{'form':form})

    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")   
            pwd=form.cleaned_data.get("password") 
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                return redirect("dish-all")
            else:
                messages.error(request,"Invalid Credentials")
                return render(request,"login.html",{"form":form}) 

class RegistrationFormView(View):
    def get(self,request,*args,**kwargs):
        form=RegistrationForm()
        return render(request,"registration.html",{'form':form})

    def post(self,request,*args,**kwargs):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            messages.success(request,"Account Created")
            return redirect("signin")
        else:
            messages.error(request,"Registration Failed")
            return render(request,"registration.html",{'form':form})              


@method_decorator(signin_required,name="dispatch")
class AddDishView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"add_dish.html")

    def post(self,request,*args,**kwargs):
        dishname=request.POST.get("dishname")   
        cat=request.POST.get("category")
        price_=request.POST.get("price")
        rating_=request.POST.get("rating") 
        Dish.objects.create(dish_name=dishname,category=cat,price=price_,rating=rating_)
        return render(request,"add_dish.html")

@method_decorator(signin_required,name="dispatch")
class DishListView(ListView):
    model=Dish
    template_name='dishlist.html'
    context_object_name='dishname'


    # def get(self,request,*args,**kwargs):
    #     dsh=Dish.objects.all()
    #     return render(request,"dishlist.html",{"dishname":dsh})

@method_decorator(signin_required,name="dispatch")
class DishDetailView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")  
        dsh=Dish.objects.get(id=id)
        return render(request,"dishdetail.html",{"dish":dsh})

@method_decorator(signin_required,name="dispatch")
class DishDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        Dish.objects.filter(id=id).delete()
        return redirect("dish-all")

@method_decorator(signin_required,name="dispatch")
class DishUpdateView(UpdateView):
    model=Dish
    form_class=DishUpdateForm
    template_name="dishupdate.html"
    pk_url_kwarg="id"
    success_url=reverse_lazy("dish-all")    


@signin_required
def signout_view(request,*args,**kwargs):
    logout(request)
    return redirect("signin")        
