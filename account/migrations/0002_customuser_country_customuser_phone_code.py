# Generated by Django 5.1.2 on 2024-10-26 04:53

import django_countries.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='country',
            field=django_countries.fields.CountryField(blank=True, max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='phone_code',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]
