from django import forms
from questions.models import MyUser,Questions
from django.contrib.auth.forms import UserCreationForm

class QuestionForm(forms.ModelForm):
    class Meta():
        model=Questions
        fields=[
            "description",
            "images"
        ]

        widgets={
            "description":forms.Textarea(attrs={"class":"form-control border border-warning mt-2","rows":3,"placeholder":"....write your question here ..."}),
            "images":forms.FileInput(attrs={"class":"form-select mt-2"})
        }


class RegistrationForm(UserCreationForm):

    password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control border border-info ","placeholder":"enter password"}))  
    password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control border border-info","placeholder":"confirm password"}))              
    
    class Meta():
        model=MyUser
        fields=['first_name','last_name','username','email',
        'phone','profile_pic']

        widgets={
            "first_name":forms.TextInput(attrs={"class":"form-control border border-info","placeholder":"enter firstname"}),
            "last_name":forms.TextInput(attrs={"class":"form-control border border-info","placeholder":"enter lastname"}),
            "username":forms.TextInput(attrs={"class":"form-control border border-info","placeholder":"enter username"}),
            "email":forms.EmailInput(attrs={"class":"form-control border border-info","placeholder":"enter email"}),
            "phone":forms.TextInput(attrs={"class":"form-control border border-info","placeholder":"enter phonenumber"}),
            
        }

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control border border-info","PlaceHolder":"..."}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control border border-info","PlaceHolder":"..."}))

class AnswerForm(forms.Form):
    answer=forms.CharField(widget=forms.Textarea(attrs={"class":"form-control","rows":3}))

