import knox.views
from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_routes, name='get routes'),
    path('login/', views.login_user, name='login'),
    path('register/', views.create_user, name='register'),
    path('logout/', knox.views.LogoutView.as_view(), name='logout'),
    path('check/', views.check_user, name='check token'),
    path('user/update_password/', views.update_password, name='change user password'),
    # path('user/update_profile/', views.update_profile, name='change user profile'),
    path('user/student/', views.get_student, name='get student details'),
]
