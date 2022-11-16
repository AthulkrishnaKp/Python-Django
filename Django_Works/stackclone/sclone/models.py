from django.db import models
from django.contrib.auth.models import User

class Questions(models.Model):
    description=models.CharField(max_length=200)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    image=models.ImageField(null=True,upload_to="images")
    created_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description

class Answers(models.Model):
    question=models.ForeignKey(Questions,on_delete=models.CASCADE)
    answer=models.CharField(max_length=200)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    upvote=models.ManyToManyField(User,related_name="upvote")
    posted_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.answer

