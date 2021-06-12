from django.contrib import admin
from django.urls import path
from sengupta_lab import views

urlpatterns = [
    path("", views.index, name='home'),
    path("research", views.research, name='research'),
    path("team", views.team, name='team'),
    path("papers", views.papers, name='papers'),
    path("softwares", views.softwares, name='softwares'),
    path("news", views.news, name='news'),
    path("about", views.about, name='about'),
]
