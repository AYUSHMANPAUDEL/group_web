from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('',views.home),
    path('blogs/<str:blog_name>/', views.blog_detail, name='blog_detail'),
]
