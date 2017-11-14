# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-12 16:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_project', models.CharField(max_length=30)),
                ('project_description', models.CharField(max_length=300)),
                ('name', models.CharField(max_length=300)),
                ('email', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='OrdersServer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=30)),
                ('time', models.CharField(max_length=30)),
                ('skype_id', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('instructions', models.CharField(max_length=300)),
                ('order_type', models.CharField(max_length=30)),
                ('tv_machine', models.CharField(max_length=30)),
                ('quantity', models.CharField(max_length=30)),
                ('payment_method', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=30)),
                ('message', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
            ],
        ),
    ]
