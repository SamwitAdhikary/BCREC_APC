# Generated by Django 3.2 on 2021-04-24 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20210425_0252'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='is_verify',
            field=models.BooleanField(default=False),
        ),
    ]
