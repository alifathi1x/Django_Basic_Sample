from django.shortcuts import render
from django.http import Http404,HttpResponse

def home_page(request):
    context = {
        "message": "Welcome to our site"
    }
    return render(request,'home_page.html',context)

def about_us(request):
    context = {
        "about_text": "Welcome to About us"

    }
    return render(request,'about_us.html',context)

def contact_us(request):
    if request.method == "POST":
        print(request.POST.get('Full Name'))
        print(request.POST.get('Email'))
        print(request.POST.get('message'))

    context = {
        "message": "Welcome to contact us",
        "about_text": "Welcome to contact us"
    }
    return render(request,"contact_us.html",context)