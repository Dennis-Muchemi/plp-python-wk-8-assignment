from django.urls import path
from . import views

urlpatterns = [
    path('', views.weather_view, name='weather'),
    path('register/', views.register, name='register'),
]
