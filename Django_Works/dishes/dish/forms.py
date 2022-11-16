from django import forms
from django.contrib.auth.models import User
from dish.models import Dish


class RegistrationForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["first_name","last_name","username","email","password"]

        widgets={
            "first_name":forms.TextInput(attrs={"class":"form-control border border-info","placeholder":"enter firstname"}),
            "last_name":forms.TextInput(attrs={"class":"form-control border border-info","placeholder":"enter lastname"}),
            "username":forms.TextInput(attrs={"class":"form-control border border-info","placeholder":"enter username"}),
            "email":forms.EmailInput(attrs={"class":"form-control border border-info","placeholder":"enter email"}),
            "password":forms.PasswordInput(attrs={"class":"form-control border border-info","placeholder":"enter password"})
        }


class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control border border-info","placeholder":"enter username"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control border border-info","placeholder":"enter password"}))      


class DishUpdateForm(forms.ModelForm):
    class Meta:
        model=Dish
        fields=["dish_name","category","price","rating"]