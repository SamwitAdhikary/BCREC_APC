# Generated by Django 3.1.7 on 2021-04-25 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0024_delete_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(default=0)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
                ('paper_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.paper')),
            ],
        ),
    ]