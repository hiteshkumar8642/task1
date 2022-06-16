from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class User_Detail(models.Model):
    email=models.CharField(max_length=40)
    lane=models.CharField(max_length=40)
    lname=models.CharField(max_length=40)
    state=models.CharField(max_length=40)
    city=models.CharField(max_length=40)
    fname=models.CharField(max_length=40)
    pin=models.CharField(max_length=40)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    pic=models.ImageField(null=True,blank=True)
    type=models.CharField(max_length=40)
