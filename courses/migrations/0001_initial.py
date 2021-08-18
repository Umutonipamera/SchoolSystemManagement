# Generated by Django 3.2.6 on 2021-08-17 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('course_name', models.CharField(max_length=12)),
                ('trainer', models.CharField(max_length=20)),
                ('trainer_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('syllabus', models.FileField(null=True, upload_to='documents/%y/%m/%d')),
                ('course_code', models.CharField(max_length=12)),
                ('description', models.TextField()),
            ],
        ),
    ]
