# Generated by Django 5.1.2 on 2024-10-23 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0003_category_course_description_course_lecturer_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='date',
            new_name='start_date',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='time',
            new_name='start_time',
        ),
        migrations.AddField(
            model_name='course',
            name='end_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='end_time',
            field=models.TimeField(null=True),
        ),
    ]