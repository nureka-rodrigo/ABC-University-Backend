import knox.views
from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_routes, name='routes'),
    path('user/', views.get_all_users, name='users'),
    path('login/', views.login_user, name='login'),
    path('register/', views.create_user, name='register'),
    path('logout/', knox.views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox.views.LogoutAllView.as_view(), name='logout all'),
    path('cookieset/', views.set_cookie, name='set cookie'),
    path('cookiedelete/', views.delete_cookie, name='delete cookie'),
]
