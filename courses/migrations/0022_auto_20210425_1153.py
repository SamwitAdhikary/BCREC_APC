# Generated by Django 3.1.7 on 2021-04-25 06:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0021_paper_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paper',
            old_name='slug',
            new_name='paperslug',
        ),
    ]
