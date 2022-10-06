from django.db import models

# Create your models here.


class Vehicles(models.Model):
    description=models.CharField(max_length=250)
    category=models.CharField(max_length=100)
    price=models.PositiveIntegerField()
    year=models.PositiveIntegerField()
    kmrun=models.PositiveIntegerField()
    place=models.CharField(max_length=120)

    def __str__(self):
        return self.description

# Vehicles.objects.create(description="Bsa Gear Cycle",category="cycle",price=4000,year=2022,kmrun=20,place="kannur")




