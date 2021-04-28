from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request, 'demo/index.html')

def signup(request):
    return render(request, 'demo/signup.html')

def dashboardMainPage(request):
    return render(request, 'demo/dashboardMainPage.html')
