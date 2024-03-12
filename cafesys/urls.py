from django.urls import path
from cafesys import views

urlpatterns = [
    path('', views.get_reviews, name='reviews'),
    path('createreview/', views.create_review, name='create_review'),
    path('review/<int:pk>/', views.get_review, name='review'),
]
