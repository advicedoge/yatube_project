
from django.shortcuts import render


def index(request):
    """Главная страница"""
    template = r'D:\Dev\yatube_project\yatube\templates\posts\index.html'
    return render(request, template)


def group_posts(request, test):
    template = r'D:\Dev\yatube_project\yatube\templates\posts\group_list.html'
    return render(request, template)
