# Generated by Django 3.1.7 on 2021-04-23 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_rename_courses_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='img_url',
        ),
    ]
