from django.shortcuts import render


def index(request):
    return render(request, 'RegistrationPage/homePage.html')

def courseReg(request):
    return render(request, 'RegistrationPage/regPage.html')

def gradPlan(request):
    return render(request, 'RegistrationPage/gradPlan.html')