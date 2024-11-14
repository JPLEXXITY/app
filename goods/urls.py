from django.urls import path
from goods import views

app_name = 'goods'  # Устанавливаем пространство имен для приложения

urlpatterns = [
    path('', views.catalog, name='index'),
    path('product/', views.product, name='product'),
]