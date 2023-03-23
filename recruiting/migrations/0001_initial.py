# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-12 15:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(blank=True, default='', max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('image_list', models.CharField(blank=True, default='', max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.CharField(blank=True, max_length=100, null=True)),
                ('title', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('description', models.CharField(blank=True, default='', max_length=100, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='company',
            name='vacancy',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='company', to='recruiting.Vacancy'),
        ),
        migrations.AddField(
            model_name='city',
            name='vacancy',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='city', to='recruiting.Vacancy'),
        ),
    ]