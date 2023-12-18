from django.urls import path
from knox.views import LogoutView

from . import views

urlpatterns = [
    path('', views.list_routes, name='list_routes'),
    path('create/', views.create_user, name='create_user'),
    path('login/', views.login_user, name='login'),
    path('register/', views.create_user, name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('user/check/', views.validate_token, name='validate_token'),
    path('user/update_password/', views.update_password, name='update_password'),
    path('user/update_profile/', views.update_profile_student, name='update_profile_student'),
    path('user/student/', views.get_student, name='get_student_details'),
    path('get_courses_prev_sem/', views.get_courses_prev_sem, name='get_course_details_of_previous_semester'),
    path('get_results/', views.get_results, name='get_result_details'),
    path('get_courses_next_sem/', views.get_courses_next_sem, name='get_course_details_of_next_semester'),
]
