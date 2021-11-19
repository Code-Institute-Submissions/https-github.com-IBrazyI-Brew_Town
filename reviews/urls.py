from django.urls import path
from . import views

urlpatterns = [
    path('', views.reviews, name='reviews'),
    path('<slug>/', views.reviews_details, name='reviews_details'),
]