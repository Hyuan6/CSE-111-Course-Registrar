from django.shortcuts import render
from django.http import HttpResponse, Http404

def index(request):
    return render(request, 'LegacyRegistrationPage/development.html')


def submit(request):
    raise Http404("Page not found. Please Reload the page.")
