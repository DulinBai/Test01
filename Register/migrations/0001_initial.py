# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-14 07:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_num', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=6)),
                ('unit', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=50)),
                ('partjob', models.CharField(max_length=50)),
                ('scheme', models.CharField(max_length=50)),
                ('password3', models.CharField(max_length=50)),
            ],
        ),
    ]
