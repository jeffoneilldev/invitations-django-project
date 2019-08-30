from django.shortcuts import render, HttpResponse, redirect, reverse
from django.contrib import auth, messages
from pages.forms import UserLoginForm

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
    messages.success(request, "You have been logged out!")
    return redirect(reverse('index'))
    
def login(request):
    """Show login page"""
    login_form = UserLoginForm()
    return render(request, 'login.html', {"login_form":login_form})