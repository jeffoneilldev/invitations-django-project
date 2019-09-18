from django.shortcuts import render, HttpResponse, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from pages.forms import UserLoginForm, UserRegistrationForm

# Create your views here.
    
def index(request):
    #bring user to home page
    return render (request, "index.html")
    
def about_page(request):
    #bring user to about page
    return render (request, "about.html")
    
@login_required
def logout(request):
    #log user out
    auth.logout(request)
    messages.success(request, "You have been logged out!")
    return redirect(reverse('index'))
    
def login(request):
    """Show login page"""
    if request.user.is_authenticated:
        return redirect(reverse('products'))
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password'])
            
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully logged in.")
                return redirect(reverse('products'))
            else:
                login_form.add_error(None, "Your Username or Password is incorrect!")
                
    else:
        login_form = UserLoginForm()
        
    return render(request, 'login.html', {"login_form":login_form})
    

def registration(request):
    """Render registration page"""
    
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered!  You now have full access to our site.")
                return redirect(reverse('index'))
            else:
                messages.error(request, "Sorry, we are unable to register your account at this time.")
    else:
        registration_form = UserRegistrationForm()
        
    return render(request, 'registration.html', {
        "registration_form": registration_form})
    

def customer_profile(request):
    """Customer profile page"""
    
    user = User.objects.get(email=request.user.email)
    return render(request, 'profile.html', {"profile": user})