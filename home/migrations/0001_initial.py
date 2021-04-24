# Generated by Django 3.2 on 2021-04-24 21:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.BigIntegerField()),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Developers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.TextField(default='')),
                ('name', models.CharField(default='', max_length=50)),
                ('image', models.ImageField(default='', upload_to='developer')),
                ('nick_name', models.CharField(default='', max_length=50)),
            ],
        ),
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
        migrations.CreateModel(
            name='UserProfileInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.BigIntegerField(blank=True, null=True)),
                ('protfolio_site', models.URLField(blank=True)),
                ('profile_pic', models.ImageField(blank=True, upload_to='pofile_pics')),
                ('course', models.CharField(choices=[('bca', 'BCA'), ('bba', 'BBA'), ('b.Tech. ME', 'B.Tech. ME'), ('b.Tech. CE', 'B.Tech. CE'), ('b.Tech. EI', 'B.Tech. EI'), ('b.Tech. EE', 'B.Tech. EE'), ('b.Tech. EC', 'B.Tech. EC'), ('b.Tech. IT', 'B.Tech. IT'), ('b.Tech. CS', 'B.Tech. CS'), ('mca', 'MCA'), ('mba', 'MBA')], default='BCA', max_length=10)),
                ('Semester', models.CharField(choices=[('first', 1), ('second', 2), ('third', 3), ('fourth', 4), ('fifth', 5), ('six', 6), ('seven', 7), ('eight', 8)], default=1, max_length=8)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
