from django.db import models
from django.contrib.auth.models import User


class Retailer(models.Model):
    
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone_number = models.IntegerField(default=00000000000)

    def __str__(self):
        return self.user.username

class Customer(models.Model):
    
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone_number = models.IntegerField(default=00000000000)
    date_birth = models.DateField(auto_now=True,verbose_name='تاریخ تولد')
    date_marraige = models.DateField(auto_now=True,verbose_name='تاریخ ازدواج')
    address = models.TextField(max_length=200)
    def __str__(self):
        return self.user.username
