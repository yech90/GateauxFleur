from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('gallery', views.gallery, name='gallery'),
    path('generic', views.generic, name='generic'),
    path('contact', views.contactView, name='contact'),
]
