from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='reviews'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='reviews_detail'),
]
