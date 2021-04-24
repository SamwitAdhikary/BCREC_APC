# Generated by Django 3.2 on 2021-04-24 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0015_delete_testmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('sem_number', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=50)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
            ],
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paper_name', models.CharField(max_length=100)),
                ('paper_code', models.CharField(max_length=100, null=True)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
                ('semester', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.semester')),
            ],
        ),
    ]
