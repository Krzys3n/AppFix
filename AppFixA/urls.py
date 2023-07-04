#"""Definiuje wzorce adresów URL dla learning_logs."""
from django.urls import path
from . import views

urlpatterns = [
# Strona główna.
path('', views.index, name='index'),
path('apps/', views.apps, name='apps'),
path('apps/(<int:app_id>)/', views.app, name='app')
]

