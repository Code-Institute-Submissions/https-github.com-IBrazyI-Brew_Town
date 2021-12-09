from django.urls import path
from . import views


urlpatterns = [
    path('', views.reviews, name='reviews'),
    path('add_review/', views.add_review, name='add_review'),
    path('edit/<int:review_id>', views.edit_review, name='edit_review'),
    path('delete/<int:review_id>', views.delete_review, name='delete_review'),
    path('review_details/<int:review_id>', views.review_details, name='review_details'),
    path('add_comment/<int:review_id>', views.add_comment, name='add_comment'),
]