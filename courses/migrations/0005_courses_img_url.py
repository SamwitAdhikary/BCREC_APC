# Generated by Django 3.2 on 2021-04-22 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20210422_2317'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='img_url',
            field=models.URLField(blank=True),
        ),
    ]
