# Generated by Django 3.2 on 2021-04-22 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_courses_img_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='img_url',
            field=models.URLField(blank=True, max_length=1000),
        ),
    ]
