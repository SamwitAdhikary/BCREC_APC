# Generated by Django 3.2 on 2021-04-22 22:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20210423_0403'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='color',
            new_name='Course',
        ),
        migrations.AlterField(
            model_name='contact',
            name='dateTime',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2021, 4, 23, 4, 3, 53, 768471)),
        ),
    ]