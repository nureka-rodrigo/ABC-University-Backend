from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.User)
admin.site.register(models.Student)
admin.site.register(models.Lecturer)
admin.site.register(models.Course)
admin.site.register(models.Degree)
admin.site.register(models.Department)
admin.site.register(models.Faculty)
admin.site.register(models.Result)
admin.site.register(models.Feedback)

