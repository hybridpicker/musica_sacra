from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('post/<int:pk>/edit/', views.blog_edit, name='blog_edit'),
    path('new', views.create_blog, name='create_blog_post'),
    path('summary', views.show_blogs_editing, name='show_blogs_editing'),
]
