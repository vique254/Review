# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-01-15 08:39
from __future__ import unicode_literals

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
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_photo', models.ImageField(blank=True, default='person.png', upload_to='images')),
                ('bio', models.CharField(max_length=200)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='images/')),
                ('image_name', models.CharField(max_length=10)),
                ('image_caption', models.CharField(max_length=250)),
                ('pub_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('comments', models.TextField()),
                ('likes', models.ManyToManyField(to='award.Project')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='award.Profile')),
            ],
        ),
    ]
