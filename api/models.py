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

    class Meta:
        verbose_name = "01. User"


# Lecturer modal
class Lecturer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    tel = models.CharField(max_length=20)

    class Meta:
        verbose_name = "02. Lecturer"


# Student modal
class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    tel = models.CharField(max_length=20)
    dob = models.DateField(null=True)
    description = models.TextField(null=True)

    class Meta:
        verbose_name = "03. Student"


# Course modal
class Course(models.Model):
    code = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    credits = models.CharField(max_length=10)
    type = models.CharField(max_length=10)

    class Meta:
        verbose_name = "04. Course"


# Degree modal
class Degree(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "05. Degree"


# Department modal
class Department(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "06. Department"


# Faculty modal
class Faculty(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "07. Facultie"


# Semester modal
class Semester(models.Model):
    name = models.CharField(max_length=20)
    status = models.CharField(max_length=20)

    class Meta:
        verbose_name = "08. Semester"


# Result modal
class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    grade = models.CharField(max_length=10)

    class Meta:
        verbose_name = "09. Result"


# Feedback modal
class Feedback(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    question = models.CharField(max_length=100)

    class Meta:
        verbose_name = "10. Feedback"
