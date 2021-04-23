# Generated by Django 3.1.7 on 2021-04-23 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_remove_contact_datetime'),
    ]

    operations = [
        migrations.CreateModel(
            name='YoutubeVideos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.CharField(default='', max_length=100)),
                ('link', models.URLField(default='')),
                ('title', models.CharField(default='', max_length=50)),
                ('image', models.ImageField(default='', upload_to='youtube')),
            ],
        ),
    ]