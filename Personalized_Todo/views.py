from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def homepage(request):
  
   return redirect("vocabulary:wordlist")
