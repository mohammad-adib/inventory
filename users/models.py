from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime

class MyUser(User):
    is_retailer = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)

class Retailer(models.Model):
    
    user = models.OneToOneField(MyUser,on_delete=models.CASCADE)
    phone_number = models.IntegerField(default=00000000000)

    def __str__(self):
        return self.user.username

class Customer(models.Model):
    
    # user = models.OneToOneField(User,on_delete=models.CASCADE)
    username = models.CharField(max_length=20, null=True)
    name = models.CharField(max_length=50, null=True) 
    phone_number = models.IntegerField(default=00000000000)
    date_birth = models.DateField(default=timezone.now,verbose_name='تاریخ تولد')
    date_marraige = models.DateField(default=timezone.now,verbose_name='تاریخ ازدواج')
    address = models.TextField(max_length=200)
    def __str__(self):
        return self.user.username


class Manager(models.Model):
    user = models.OneToOneField(MyUser,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
