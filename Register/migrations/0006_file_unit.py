# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-21 02:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Register', '0005_auto_20170315_1319'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id_num', models.AutoField(primary_key=True, serialize=False)),
                ('file_name', models.CharField(default='', max_length=50)),
                ('schoolmaster', models.CharField(default='', max_length=50)),
                ('dean', models.CharField(default='', max_length=50)),
                ('teacher', models.CharField(default='', max_length=50)),
                ('student', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id_num', models.AutoField(primary_key=True, serialize=False)),
                ('unit_name', models.CharField(max_length=50)),
            ],
        ),
    ]
