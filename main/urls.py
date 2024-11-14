from django.urls import path
from main import views

app_name = 'main'  # Устанавливаем пространство имен для приложения

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]