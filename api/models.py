from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=40)
    age = models.IntegerField(null = False, default = 2)
    numLegs = models.IntegerField(null = False, default = 2)