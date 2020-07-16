from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def homepage(request):
  
   return render(request,'todo/home.html')
