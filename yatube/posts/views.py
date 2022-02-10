
from django.http import HttpResponse


def index(request):
    """Главная страница"""
    return HttpResponse('Главная страница')


def group_posts(request, test):
    return HttpResponse(test)
