from django.contrib.auth.models import AbstractUser
from django.db import models


# User modal
class User(AbstractUser):
    username = models.CharField(max_length=100, primary_key=True)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=20)

    last_login = None
    is_superuser = None
    is_staff = None
    date_joined = None
    email = None
    first_name = None
    last_name = None

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [username, password, role]


# Degree modal
class Degree(models.Model):
    name = models.CharField(max_length=100, null=False)


# Department modal
class Department(models.Model):
    name = models.CharField(max_length=100, null=False)


# Faculty modal
class Faculty(models.Model):
    name = models.CharField(max_length=100, null=False)


# Lecturer modal
class Lecturer(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    tel = models.CharField(max_length=20, null=True)
    image = models.CharField(max_length=100, null=True)


# Student modal
class Student(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    degree = models.ForeignKey(Degree, on_delete=models.CASCADE, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, null=True)
    tel = models.CharField(max_length=20, null=True)
    dob = models.DateField(null=True)
    description = models.TextField(null=True)
    image = models.CharField(max_length=100, null=True)


# Course modal
class Course(models.Model):
    code = models.CharField(max_length=100, null=False)
    title = models.CharField(max_length=100, null=False)
    credits = models.CharField(max_length=10, null=False)
    type = models.CharField(max_length=10, null=False)


# Semester modal
class Semester(models.Model):
    name = models.CharField(max_length=20, null=False)
    status = models.CharField(max_length=20, null=True)
