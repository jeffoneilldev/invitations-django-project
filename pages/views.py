from django.shortcuts import render, HttpResponse

# Create your views here.
def say_hello(request):
    #testing view
    return HttpResponse("Hi There!")
    
def goto_home_page(request):
    #bring user to home page
    return render (request, "index.html")
    
def about_page(request):
    #bring user to about page
    return render (request, "about.html")