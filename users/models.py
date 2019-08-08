from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime
from stores.models import Store

class Retailer(models.Model):
    
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone_number = models.IntegerField(default=00000000000)

    def __str__(self):
        return self.user.username


    ######## R E L A T I O N S H I P S ########    

    store = models.ForeignKey(Store,blank=True,on_delete=models.CASCADE,related_name='store')

class Customer(models.Model):
    
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone_number = models.IntegerField(default=00000000000)
    date_birth = models.DateField(default=timezone.now,verbose_name='تاریخ تولد')
    date_marraige = models.DateField(default=timezone.now,verbose_name='تاریخ ازدواج')
    address = models.TextField(max_length=200)
    def __str__(self):
        return self.user.username
