from django.shortcuts import render
from django.http import HttpResponse, Http404

import sqlite3

def index(request):
    if request.method == 'POST':
        form = request.POST.dict()
        for key, value in form.items():
            print(f"{key} {value}")

    return render(request, 'LegacyRegistrationPage/LegacyRegistrationPage.html')

