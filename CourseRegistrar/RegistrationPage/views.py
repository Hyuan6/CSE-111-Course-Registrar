from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'RegistrationPage/homePage.html')

def courseReg(request):
    return render(request, 'RegistrationPage/regPage.html')

def gradPlan(request):
    return render(request, 'RegistrationPage/development.html')

