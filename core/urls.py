from django.contrib import admin
from django.urls import path
from core import views

 

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('exams/', views.exams, name='exams'),
    path('results/', views.results, name='results'),
   
]
