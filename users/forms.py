from django import forms
from django.contrib.auth.models import User
from .models import MyUser, Retailer, Customer

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = MyUser
        fields = ('username','email','password')



class RetailerForm(forms.ModelForm):
    class Meta():
        model = Retailer
        fields = ('phone_number',)

class CustomerForm(forms.ModelForm):
    class Meta():
        model = Customer
        fields = ('phone_number', 'date_birth', 'date_marraige', 'address')


