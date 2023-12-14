# Generated by Django 5.0 on 2023-12-14 16:40

import django.utils.timezone
from django.db import migrations, models

import api.models


class Migration(migrations.Migration):
    dependencies = [
        ('api', '0006_alter_lecturer_image_alter_student_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lecturer',
            name='image',
        ),
        migrations.RemoveField(
            model_name='student',
            name='image',
        ),
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to=api.models.upload_to,
                                    verbose_name='Image'),
            preserve_default=False,
        ),
    ]
