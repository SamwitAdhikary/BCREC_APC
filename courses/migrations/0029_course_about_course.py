# Generated by Django 3.1.7 on 2021-04-25 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0028_remove_paper_paperslug'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='about_course',
            field=models.TextField(default=''),
        ),
    ]
