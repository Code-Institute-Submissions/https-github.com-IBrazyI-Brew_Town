from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('index/', views.newsletter_email, name='newsletter_email'),
]
