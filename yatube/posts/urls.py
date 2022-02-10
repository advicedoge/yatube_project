"""
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path("group/<slug:test>/", views.group_posts, name="group_list")
]
