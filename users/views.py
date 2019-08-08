from django.shortcuts import render
from users.forms import UserForm, CustomerForm, RetailerForm
from .models import MyUser
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse, JsonResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


#home page
def index(request):
    return render(request,'homepage/index.html')


def retailers(request):
    return render(request,'users/retailers.html')

def managers(request):
    return render(request,'users/managers.html')

#register managers

def register_customer(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        customer_form = CustomerForm(data=request.POST)
        if user_form.is_valid() and customer_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            customer = customer_form.save(commit=False)
            customer.user = user

  
            customer.save()
            registered = True
        else:
            print(user_form.errors,customer_form.errors)
    else:
        user_form = UserForm()
        customer_form = CustomerForm()

    return render(request,'users/register_customer.html',
                                          {'user_form':user_form,
                                           'customer_form':customer_form,
                                           'registered':registered})


#login
def get_user(email):
    try:
        return MyUser.objects.get(email=email.lower())
    except MyUser.DoesNotExist:
        return None

def user_login(request):
    loggedin = False
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = get_user(email)
        user = authenticate(username=username,password=password)
        

        if user:
            if user.is_active:
                login(request,user)            
                loggedin = True
            else:
                return JsonResponse({
                'status':False,
                'message' : 'You are noy activated'})
        else:
            return JsonResponse({
            'status':False,
            'message' : 'Your username and password did not mach. Try again' })
    else:
        return render(request,'users/login.html',{})

    return HttpResponseRedirect(reverse('index'))







#logout part

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
