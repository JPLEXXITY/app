from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    context: dict[str, str] = {
        'title': 'Home',
        'content': 'Главная страница магазина - Home',
        'list': ['first', 'second', 'third', 'fourth'],
        'dict': {'first': 1},
        'bool': True,
    }
    
    return render(request, 'main/index.html', context)

def about(request):
    return HttpResponse('About page')