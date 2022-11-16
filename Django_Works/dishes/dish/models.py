from django.db import models

# Create your models here.

class Dish(models.Model):
    dish_name=models.CharField(max_length=100)
    category=models.CharField(max_length=200)
    price=models.PositiveIntegerField()
    rating=models.PositiveIntegerField()

    def __str__(self): 
        return self.dish_name