
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import Count
# Create your models here.

class MyUser(AbstractUser):
    phone=models.CharField(max_length=200)
    profile_pic=models.ImageField(null=True,upload_to="profilepics",blank=True)


class Questions(models.Model):
    description=models.CharField(max_length=200)
    user=models.ForeignKey(MyUser,on_delete=models.CASCADE)
    images=models.ImageField(null=True,upload_to="images",blank=True)
    created_date=models.DateField(auto_now_add=True)
    is_active=models.BooleanField(default=True)


    @property
    def fetch_answers(self):
        answers=self.answers_set.all().annotate(u_count=Count('upvote')).order_by('-u_count')
        return answers 

    def __str__(self):
        return self.description

    
class Answers(models.Model):
    question=models.ForeignKey(Questions,on_delete=models.CASCADE)
    answer=models.CharField(max_length=200)
    user=models.ForeignKey(MyUser,on_delete=models.CASCADE)   
    upvote=models.ManyToManyField(MyUser,related_name="upvote")
    created_date=models.DateField(auto_now_add=True)  

    def __str__(self):
        return self.answer
    
