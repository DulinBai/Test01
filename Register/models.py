# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):

    id_num = models.CharField(max_length=50 , primary_key=True)
    username = models.CharField(max_length=50, default='')
    gender = models.CharField(max_length=6, default='')
    unit = models.CharField(max_length=50, default='')
    position = models.CharField(max_length=50, default='')
    partjob = models.CharField(max_length=50, default='')
    scheme = models.CharField(max_length=50, default='')
    password_based = models.CharField(max_length=50)
    field = models.CharField(max_length=50, default='')

class Unit(models.Model):
    id_num = models.AutoField(primary_key=True)
    unit_name = models.CharField(max_length=50)

class File_Authority(models.Model):
    id_num = models.AutoField(primary_key=True)
    file_name = models.CharField(max_length=50, default='')
    schoolmaster = models.CharField(max_length=50, default='')
    dean = models.CharField(max_length=50, default='')
    teacher = models.CharField(max_length=50, default='')
    student = models.CharField(max_length=50, default='')

class File(models.Model):
    id_num = models.AutoField(primary_key=True)
    file_name = models.CharField(max_length=50, default='')
    schoolmaster = models.CharField(max_length=50, default='')
    dean = models.CharField(max_length=50, default='')
    teacher = models.CharField(max_length=50, default='')
    student = models.CharField(max_length=50, default='')