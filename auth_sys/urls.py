from django.urls import path
from auth_sys import views

urlpatterns = [
    path('accounts/login/', views.register, name='register'),
    
]