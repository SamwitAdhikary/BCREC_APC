# Generated by Django 3.2 on 2021-04-24 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20210425_0250'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='name',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
