# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-10 09:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(verbose_name='created date')),
                ('title', models.CharField(max_length=1000, verbose_name='title')),
                ('content', models.TextField(verbose_name='content')),
            ],
        ),
        migrations.CreateModel(
            name='Blogger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(verbose_name='created date')),
                ('creator_id', models.TextField(verbose_name='creator id')),
                ('FirstName', models.CharField(max_length=100, verbose_name='first name')),
                ('LastName', models.CharField(max_length=100, verbose_name='last name')),
                ('content', models.TextField(verbose_name='content')),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Blogger'),
        ),
    ]
