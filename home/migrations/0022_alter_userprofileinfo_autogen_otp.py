# Generated by Django 3.2 on 2021-04-25 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_rename_otp_userprofileinfo_autogen_otp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='autogen_otp',
            field=models.IntegerField(),
        ),
    ]
