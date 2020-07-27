#from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='letter_tracking-home'),
    path('about/', views.about, name='letter_tracking-about'),
]
