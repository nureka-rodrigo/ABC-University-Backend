from django.urls import path
from knox.views import LogoutView

from . import views

urlpatterns = [
    path('', views.list_routes, name='list_routes'),
    path('login/', views.login_user, name='login'),
    path('register/', views.create_user, name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('user/check/', views.validate_token, name='validate_token'),
    path('user/update_password/', views.update_password, name='update_password'),
    path('user/update_profile/', views.update_profile_student, name='update_profile_student'),
    path('user/student/', views.get_student, name='get_student_details'),
    path('get_result/', views.get_result, name='get_result_details'),
]
