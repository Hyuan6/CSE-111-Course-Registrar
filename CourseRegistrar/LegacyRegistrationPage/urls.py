from django.urls import path
from . import views

app_name = 'LegReg'
urlpatterns = [
    path('', views.index, name='index'),
]