# Create your models here.
from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=255)
    ammount = models.IntegerField()
    description = models.TextField()
    price = models.IntegerField()
    