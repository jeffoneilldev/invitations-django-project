from django.shortcuts import render, HttpResponse, redirect, reverse
from django.contrib import auth

# Create your views here.
def say_hello(request):
    #testing view
    return HttpResponse("Hi There!")
    
def index(request):
    #bring user to home page
    return render (request, "index.html")
    
def about_page(request):
    #bring user to about page
    return render (request, "about.html")
    
def logout(request):
    #log user out
    auth.logout(request)
    return redirect(reverse('index'))