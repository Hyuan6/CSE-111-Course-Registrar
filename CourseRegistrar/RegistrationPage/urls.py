from django.urls import path
from . import views

app_name = 'CourseReg'
urlpatterns = [
    path('', views.index, name='index'),
    path('RegPage/', views.courseReg, name='RegPage'),
    path('GradPlan/', views.gradPlan, name='GradPlan'),
]