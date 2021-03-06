from django.shortcuts import render,HttpResponseRedirect
from django. http import HttpResponse
from django.urls import reverse

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout,authenticate

from django.contrib.auth.decorators import login_required
# Create your views here.

def signup(request):
    form=UserCreationForm()
    
    registered=False
    if request.method=="POST":
        form=UserCreationForm(data=request.POST)
        if form.is_valid:
            form.save()
            registered=True
    context={'form':form,'registered':registered}
    return render(request,'authentication/signup.html',context)

def login_page(request):
    form=AuthenticationForm()
    if request.method=="POST":
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse('vocabulary:wordlist'))
    context={'form':form}
    return render(request,'authentication/login.html',context)

@login_required

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))