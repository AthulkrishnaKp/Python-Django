from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Books(models.Model):
    name=models.CharField(max_length=200)
    author=models.CharField(max_length=120)
    price=models.PositiveIntegerField()
    publisher=models.CharField(max_length=200)
    qty=models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name

class Reviews(models.Model):
    book=models.ForeignKey(Books,on_delete=models.CASCADE)    # Foreign key
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    comment=models.CharField(max_length=150)
    rating=models.PositiveIntegerField()
    create_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment

class Carts(models.Model):
    book=models.ForeignKey(Books,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    options=(
        ("in-cart","in-cart"),
        ("cancelled","cancelled"),
        ("order-placed","order-placed")
    )
    status=models.CharField(max_length=120,choices=options,default="in-cart")


