from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Library
from django.template import loader
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout 
from .forms import UserCreationForm, LoginForm, RegisterForm
from django.contrib import messages


# Create your views here.

def base(request):
    return render(request,'t_app_jlims/base.html')

# Library page
def librarypage(request):
  mydata = Library.objects.all().values()
  template = loader.get_template('t_app_jlims/library.html')
  context = {
    'mybooks': mydata,
  }
  return HttpResponse(template.render(context, request))



# login page
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return render(request, 't_app_jlims/base.html', {'form': form}) 
    else:
        form = LoginForm()
    return render(request, 't_app_jlims/login.html', {'form': form})


# logout page

def user_logout(request):
    logout(request)
    return redirect('login')

 # Registration
def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 't_app_jlims/register.html', {'form': form})    
   
    if request.method == 'POST':
        form = RegisterForm(request.POST) 
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'You have singed up successfully.')
            login(request, user)
            return redirect('login')
        else:
            return render(request, 't_app_jlims/register.html', {'form': form})