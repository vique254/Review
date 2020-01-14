# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-01-14 11:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='home')),
                ('image_name', models.CharField(max_length=10)),
                ('image_caption', models.CharField(max_length=250)),
                ('comments', models.TextField()),
                ('likes', models.ManyToManyField(to='award.Image')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_photo', models.ImageField(default='', height_field=200, upload_to='profile', width_field=200)),
                ('bio', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='image',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='award.Profile'),
        ),
    ]