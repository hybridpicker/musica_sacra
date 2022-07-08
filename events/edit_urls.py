from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/edit/', views.event_edit, name='event_edit_detail'),
    path('new', views.create_event, name='create_event'),
    path('all-events', views.show_events_editing, name='show_events_editing'),
]
