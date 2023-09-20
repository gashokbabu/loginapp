from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate
from django.http import HttpResponse
# Create your views here.

def loginView(request):
    if request.method=='POST':
        # step:1 :- Getting Form details
        username = request.POST.get('username')
        organisation = request.POST.get('organisation')
        password = request.POST.get('password')

        # step:2 :-Chanking the user entered correct username/organisation or not
        try:
            user = User.objects.get(username=username,organisation=organisation)
        except User.DoesNotExist:
            messages.error(request,'Please enter correct Username/Organisation details')
            return render(request,'login.html')
        except:
            messages.error(request,'Something went Wrong')
            return render(request,'login.html',)

        # step:3 :-Checking password
        auth = authenticate(request,username=username,password=password)
        if auth:
            return redirect('/user/success/')
        else:
            messages.error(request,'Password is incorrect.Please enter correct Password')
            return render(request,'login.html')
    return render(request,'login.html')


def loginSuccess(request):
    return HttpResponse("<h1>successfully logged in</h1>", content_type='text/html', charset='utf-8')