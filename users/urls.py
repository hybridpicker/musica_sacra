from django.urls import path, include
from . import views
from .views import UsersHomePageView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('', UsersHomePageView.as_view(), name='user_home'),
    path('password/change', views.change_password, name='change_password'),
    path('password/sucess', views.change_password_success, name='change_password_success'),
]
