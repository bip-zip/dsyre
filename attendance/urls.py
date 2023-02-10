from django.contrib import admin
from django.urls import path, include
from . import views
app_name = 'attendance'

urlpatterns = [
    path('', views.AHome.as_view()),
    
]
