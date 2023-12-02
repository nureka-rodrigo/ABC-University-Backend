from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_routes, name='routes'),
    path('user/', views.get_all_users, name='users'),
    path('login/', views.user_login, name='login'),
    path('register/', views.create_user, name='register'),
]
