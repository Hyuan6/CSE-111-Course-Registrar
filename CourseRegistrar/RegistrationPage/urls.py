from django.urls import path
from . import views


app_name = 'CourseReg'
urlpatterns = [
    path('', views.index, name='index'),
    path('RegPage/', views.courseReg, name='RegPage'),
    path('GradPlan/', views.gradPlan, name='GradPlan'),
    path('ajax/', views.search_bar, name='tk'),
    path('register/', views.reg_for, name='register'),
    path('pref/', views.est_pref,name='pref')
    path('student_profile/', views.student_profile, name='sp'),
]