# Generated by Django 3.1.7 on 2021-04-26 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20210426_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='phone_number',
            field=models.CharField(default='', max_length=20),
        ),
    ]