# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-14 08:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Register', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.AlterField(
            model_name='user',
            name='id_num',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
