
from django.shortcuts import render,redirect

# Create your views here.

from questions.forms import RegistrationForm,LoginForm,QuestionForm,AnswerForm
from django.views.generic import CreateView,FormView,ListView,DetailView,DeleteView
from questions.models import Answers, MyUser,Questions
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache


def signin_required(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            return redirect("signin")
        else:
            return fn(request,*args,**kwargs)    
    return wrapper

decs=[signin_required,never_cache]

@method_decorator(decs,name="dispatch")
class HomeView(CreateView,ListView):
    template_name='home.html'
    form_class=QuestionForm
    model=Questions
    success_url=reverse_lazy('home')
    context_object_name="questions"

    def get_queryset(self):
        return Questions.objects.all().exclude(user=self.request.user)

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)

                #   OR

    # def post(self,request,*args,**kwargs):
    #     form=QuestionForm(request.post)
    #     if form.is_valid:
    #         quest=form.save(commit=False)
    #         quest.user=request.user
    #         quest.save()
    #         return redirect("home")


class MyQuestionsView(ListView):
    model=Questions
    template_name="myquestions.html"
    context_object_name='myquestions'

    def get_queryset(self):
        return Questions.objects.filter(user=self.request.user)

class SignupView(CreateView):
    model=MyUser    
    form_class=RegistrationForm
    template_name='register.html'
    success_url=reverse_lazy("signin")

def signout_view(request,*args,**kwargs):
    logout(request)
    return redirect("signin")


class LoginFormView(FormView):
    form_class=LoginForm
    template_name='login.html'

    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)   
        if form.is_valid():
            uname=form.cleaned_data.get("username")   
            pwd=form.cleaned_data.get("password") 
            usr=authenticate(request,username=uname,password=pwd) 
            if usr:
                login(request,usr)
                return redirect('home')
            else:                            
                return render(request,"login.html",{"form":form})


@method_decorator(decs,name="dispatch")
class QuestionDetailView(DetailView,FormView):
    model=Questions
    template_name="question-detail.html"
    pk_url_kwarg="id"
    context_object_name="question"
    form_class=AnswerForm


decs
def add_answer(request,*args,**kwargs):
    if request.method=="POST":
        form=AnswerForm(request.POST)
        if form.is_valid():
            answer=form.cleaned_data.get("answer")
            qid=kwargs.get("id")
            question=Questions.objects.get(id=qid)
            Answers.objects.create(question=question,answer=answer,user=request.user)
            return redirect('home')
        else:
            return redirect('home')    


decs
def upvote_view(request,*args,**kwargs):
    ans_id=kwargs.get("id")
    ans=Answers.objects.get(id=ans_id)
    ans.upvote.add(request.user)
    ans.save()
    return redirect("home")

def remove_answer(request,*args,**kwargs):
    ans_id=kwargs.get("id")
    Answers.objects.get(id=ans_id).delete()
    return redirect("home")