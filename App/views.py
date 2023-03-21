from django.shortcuts import render


# Create your views here.

def GetHomePage (request):
    return render(request , 'home.html')

def GetAboutPage(request):
    return render(request , 'about.html')