from django.db import models
from categories.models import Category


class Event(models.Model):
    name = models.CharField(max_length=30)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,blank=True,null=True)

    date= models.DateField(null=True,blank=True)
    location = models.CharField(max_length=50)
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.name