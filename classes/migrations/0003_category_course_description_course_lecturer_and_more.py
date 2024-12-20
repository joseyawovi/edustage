# Generated by Django 5.1.2 on 2024-10-22 07:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0002_registration'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='lecturer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lectured_courses', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='course',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='liked_courses', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='course',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='classes.category'),
        ),
    ]
