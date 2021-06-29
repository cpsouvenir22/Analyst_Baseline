from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('user/register', views.register),
    path('user/login', views.login),
    path('user/logout', views.logout),
    
]